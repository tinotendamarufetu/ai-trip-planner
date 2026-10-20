from langgraph.graph import StateGraph, START, END
from state import TravelState
from database import get_checkpointer

from agents import (
    ROUTE_MAP, 
    budget_agent, 
    budget_agent, 
    flight_agent, 
    guardrail_blocked_agent, 
    human_approval_agent,  
    hotel_agent, 
    final_agent, 
    supervisor_agent, supervisor_agent, 
    weather_agent,
    itinerary_agent,
    route_from_supervisor,
    route_after_agent
)


def build_travel_graph():
    graph = StateGraph(TravelState)

    graph.add_node("supervisor", supervisor_agent)
    graph.add_node("guardrail_blocked", guardrail_blocked_agent)
    graph.add_node("flight_agent", flight_agent)
    graph.add_node("hotel_agent", hotel_agent)
    graph.add_node("weather_agent", weather_agent)
    graph.add_node("budget_agent", budget_agent)
    graph.add_node("itinerary_agent", itinerary_agent)
    graph.add_node("human_approval", human_approval_agent)
    graph.add_node("final_agent", final_agent)

    graph.add_edge(START, "supervisor")
    graph.add_conditional_edges("supervisor", route_from_supervisor, ROUTE_MAP)

    graph.add_conditional_edges(
        "flight_agent", route_after_agent("flight_agent"), ROUTE_MAP
    )
    graph.add_conditional_edges(
        "hotel_agent", route_after_agent("hotel_agent"), ROUTE_MAP
    )
    graph.add_conditional_edges(
        "weather_agent", route_after_agent("weather_agent"), ROUTE_MAP
    )
    graph.add_conditional_edges(
        "budget_agent", route_after_agent("budget_agent"), ROUTE_MAP
    )

    graph.add_edge("itinerary_agent", "human_approval")
    graph.add_edge("human_approval", "final_agent")
    graph.add_edge("final_agent", END)
    graph.add_edge("guardrail_blocked", END)

    checkpointer = get_checkpointer()
    return graph.compile(checkpointer=checkpointer)

travel_graph = build_travel_graph()