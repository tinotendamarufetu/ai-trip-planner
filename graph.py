from langgraph.graph import StateGraph, START, END
from state import TravelState
from agents import flight_agent, hotel_agent, itinerary_agent, final_agent
from database import get_checkpointer

def build_travel_graph():
    graph = StateGraph(TravelState)

    graph.add_node("flight_agent", flight_agent)
    graph.add_node("hotel_agent", hotel_agent)
    graph.add_node("itinerary_agent", itinerary_agent)
    graph.add_node("final_agent", final_agent)

    graph.add_edge(START, "flight_agent")
    graph.add_edge("flight_agent", "hotel_agent")
    graph.add_edge("hotel_agent", "itinerary_agent")
    graph.add_edge("itinerary_agent", "final_agent")
    graph.add_edge("final_agent", END)

    checkpointer = get_checkpointer()
    return graph.compile(checkpointer=checkpointer)

travel_graph = build_travel_graph()