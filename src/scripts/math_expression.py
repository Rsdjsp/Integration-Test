"""
Evaluate math expression
"""
def evaluate_expression(expression: str) -> float:
    """
    Evaluate
    """
    try:
        result = eval(expression)
        return result
    except Exception as e:
        raise ValueError(f"Invalid mathematical expression: {expression}") from e