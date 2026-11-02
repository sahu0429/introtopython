import ast
import math

_ALLOWED_BINOPS = {
    ast.Add: lambda a, b: a + b,
    ast.Sub: lambda a, b: a - b,
    ast.Mult: lambda a, b: a * b,
    ast.Div: lambda a, b: a / b,
    ast.FloorDiv: lambda a, b: a // b,
    ast.Mod: lambda a, b: a % b,
    ast.Pow: lambda a, b: a ** b,
}

_ALLOWED_UNARYOPS = {
    ast.UAdd: lambda a: +a,
    ast.USub: lambda a: -a,
}


def safe_eval(expr: str):
    node = ast.parse(expr, mode="eval")

    def _eval(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op = type(node.op)
            if op not in _ALLOWED_BINOPS:
                raise ValueError(f"Unsupported operator: {ast.dump(node.op)}")
            return _ALLOWED_BINOPS[op](left, right)
        if isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            op = type(node.op)
            if op not in _ALLOWED_UNARYOPS:
                raise ValueError(f"Unsupported unary operator: {ast.dump(node.op)}")
            return _ALLOWED_UNARYOPS[op](operand)
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("Only direct function calls are allowed.")
            if node.func.id not in {"abs", "round", "sqrt", "sin", "cos", "tan"}:
                raise ValueError(f"Unsupported function: {node.func.id}")
            if len(node.args) != 1:
                raise ValueError("Functions require exactly one argument.")
            arg = _eval(node.args[0])
            funcs = {
                "abs": abs,
                "round": round,
                "sqrt": math.sqrt,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
            }
            return funcs[node.func.id](arg)
        raise ValueError(f"Unsupported expression: {ast.dump(node)}")

    return _eval(node.body)


def main():
    print("Simple Calculator")
    print("Type 'q' to quit.")

    while True:
        expr = input("Expression: ").strip()
        if expr.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break

        try:
            result = safe_eval(expr)
            print(f"Result: {result}")
        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
