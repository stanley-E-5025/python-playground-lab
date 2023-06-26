from dataclasses import asdict, astuple, dataclass, field


class CustomGraph:
    def __init__(self, name: str, edges: list, vertices: int):
        if not isinstance(name, str):
            print("name should be of type str")
        if not isinstance(edges, list):
            print("edges should be of type list")
        if not isinstance(vertices, int):
            print("vertices should be of type int")
        self.name = name
        self.edges = edges
        self.vertices = vertices

    def add_edge(self, edge):
        self.edges.append(edge)
        self.vertices += 1

    def remove_edge(self, edge):
        self.edges.remove(edge)
        self.vertices -= 1


@dataclass
class Algorithm:
    complexity: str
    name: str
    description: str
    formulas: list = field(default_factory=list)
    execution_graph: CustomGraph = field(default_factory=lambda: CustomGraph(name="Execution Graph", edges=[], vertices=0))

    def __post_init__(self):
        if not isinstance(self.complexity, str):
            print("complexity should be of type str")
        if not isinstance(self.name, str):
            print("name should be of type str")
        if not isinstance(self.description, str):
            print("description should be of type str")
        if not isinstance(self.formulas, list):
            print("formulas should be of type list")
        if not isinstance(self.execution_graph, CustomGraph):
            print("execution_graph should be of type CustomGraph")

    def add_formula(self, formula):
        self.formulas.append(formula)

    def remove_formula(self, formula):
        self.formulas.remove(formula)

    def to_dict(self):
        return asdict(self)

    def to_tuple(self):
        return astuple(self)


def main():
    algorithm = Algorithm(complexity="O(n)", name="Pythagorean", description="Pythagorean theorem")
    algorithm.add_formula("a^2 + b^2 = c^2")
    algorithm.execution_graph.add_edge((1, 2))
    print(algorithm.to_dict())
    print(algorithm.to_tuple())


if __name__ == "__main__":
    main()
