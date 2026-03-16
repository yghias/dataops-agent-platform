from tools.query_optimizer import QueryOptimizer


def test_query_optimizer_flags_select_star() -> None:
    result = QueryOptimizer().analyze("select * from analytics.orders")
    assert result["score"] < 100
    assert any("select *" in warning.lower() for warning in result["warnings"])


def test_query_optimizer_returns_recommendations() -> None:
    result = QueryOptimizer().analyze("select customer_id from analytics.orders")
    assert result["recommendations"]
