from __future__ import annotations

from pydantic import BaseModel

from .annotated_trace import Trace


class TraceNode(Trace):
    parent: str | None
    children: list[str]

    def get_balance_diff(self) -> int | None:
        if not self.annotations:
            return None
        for annotation in self.annotations:
            if annotation.name == "balance_changed":
                return annotation.data.balance_diff

    def get_jetton_address(self) -> str | None:
        if not self.annotations:
            return None
        for annotation in self.annotations:
            if annotation.name == "ft_internal_transfer":
                return annotation.data.jetton_address

    def get_amount(self) -> str | None:
        if not self.annotations:
            return None
        for annotation in self.annotations:
            if annotation.name == "ft_internal_transfer":
                return int(annotation.data.amount)

    def get_ft_transfer_amount(self) -> str | None:
        if not self.annotations:
            return None
        for annotation in self.annotations:
            if annotation.name == "ft_transfer":
                return int(annotation.data.amount)

    def get_burn_amount(self) -> str | None:
        if not self.annotations:
            return None
        for annotation in self.annotations:
            if annotation.name == "ft_burn_notification":
                return int(annotation.data.amount)

    def is_burned(self) -> bool:
        if not self.annotations:
            return False
        return "ft_burn_notification" in [annotation.name for annotation in self.annotations]


class TraceNodes(BaseModel):
    nodes: dict[str, TraceNode]

    @classmethod
    def parse_trace(cls, obj: Trace) -> TraceNodes:
        def parse(trace: Trace, parent_hash: str | None) -> None:
            nodes[trace.hash] = trace.dict(exclude={"children"})
            nodes[trace.hash]["children"] = [child.hash for child in trace.children] if trace.children else []
            nodes[trace.hash]["parent"] = parent_hash
            if trace.children:
                for trace_child in trace.children:
                    parse(trace_child, trace.hash)

        nodes = {}
        parse(obj, None)
        return super().parse_obj({"nodes": nodes})

    def get(self, hash: str) -> TraceNode | None:
        return self.nodes.get(hash, None)

    def get_jetton_transfer_child(self, hash: str, level: int) -> TraceNode | None:
        hashes = [hash]
        for _ in range(level):
            hashes = [
                child_hash for hash in hashes for child_hash in self.get(hash).children if self.get(hash).children
            ]
        for hash in hashes:
            if self.get(hash).annotations:
                for annotation in self.get(hash).annotations:
                    if annotation.name == "ft_internal_transfer":
                        return self.get(hash)

    def get_jetton_transfer_children(self, hash: str, level: int) -> list[TraceNode] | None:
        hashes = [hash]
        for _ in range(level):
            hashes = [
                child_hash for hash in hashes for child_hash in self.get(hash).children if self.get(hash).children
            ]
        nodes = []
        for hash in hashes:
            if self.get(hash).annotations:
                for annotation in self.get(hash).annotations:
                    if annotation.name == "ft_internal_transfer":
                        nodes.append(self.get(hash))
        return nodes

    def get_address(self, hash: str) -> str | None:
        return self.get(hash).account.address if self.get(hash) else None

    def get_parent(self, hash: str, level: int) -> TraceNode | None:
        parent_node = self.get(hash)
        for _ in range(level):
            if not parent_node:
                return None
            parent_node = self.get(parent_node.parent)
            hash = parent_node.hash if parent_node else None
        return parent_node

    def get_parent_hash(self, hash: str, level: int) -> str | None:
        parent_node = self.get_parent(hash, level)
        return parent_node.hash if parent_node else None

    def get_parent_address(self, hash: str, level: int) -> str | None:
        parent_node = self.get_parent(hash, level)
        return parent_node.account.address if parent_node else None

    def get_list_by_address(self, address: str) -> list[TraceNode]:
        return [node for node in self.nodes.values() if node.account.address == address]

    def get_hashes_by_address(self, address: str) -> list[str]:
        return [node.hash for node in self.nodes.values() if node.account.address == address]

    def get_children_addresses(self, hash: str) -> list[str]:
        node = self.get(hash)
        if not node:
            return []
        return [self.get_address(child_hash) for child_hash in node.children]

    def get_child_by_address(self, hash: str, address: str) -> TraceNode | None:
        node = self.get(hash)
        for child_hash in node.children:
            if self.get_address(child_hash) == address:
                return self.get(child_hash)
        return None

    def count_transactions(self, start_hash: str) -> int:
        def counter(hash: str, start_address: str) -> None:
            count = 1
            node = self.get(hash)
            for child_hash in node.children:
                if self.get_address(child_hash) != start_address:
                    count += counter(child_hash, start_address)
                else:
                    count += 1
            return count

        return counter(start_hash, self.get(start_hash).account.address)
