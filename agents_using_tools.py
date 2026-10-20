from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from state import TravelState
import os

# Import the tools for flight search and Tavily search, which will be used in the hotel_agent function to perform a search using the Tavily MCP server.
from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights


llm = ChatGroq(model="qwen/qwen3.8-27b", api_key=os.getenv("GROQ_API_KEY"))

def flight_agent(state: TravelState):
    query = state["user_query"]
    flight_data = search_flights(query)
    return {
        "flight_results": flight_data,
        "messages": [AIMessage(content="Flight results fetched.")],
        "llm_calls": state.get("llm_calls", 0) + 1
    }

def hotel_agent(state: TravelState):
    query = f"Best hotels for {state['user_query']}"
    hotel_results = tavily_search(query)
    return {
        "hotel_results": hotel_results,
        "messages": [AIMessage(content="Hotel information fetched.")],
        "llm_calls": state.get("llm_calls", 0) + 1
    }

def itinerary_agent(state: TravelState):
    prompt = f"""
    Create a complete travel itinerary.
    User Query: {state['user_query']}
    Flight Results: {state['flight_results']}
    Hotel Results: {state['hotel_results']}
    Make the itinerary practical, budget-aware, and easy to follow.
    """
    response = llm.invoke([SystemMessage(content="You are an expert travel planner."), HumanMessage(content=prompt)])
    return {
        "itinerary": response.content,
        "messages": [response],
        "llm_calls": state.get("llm_calls", 0) + 1
    }

def final_agent(state: TravelState):
    final_prompt = f"""
    Generate the final travel response for the user.
    User Request: {state['user_query']}
    Flights: {state['flight_results']}
    Hotels: {state['hotel_results']}
    Itinerary: {state['itinerary']}
    Format beautifully with: Trip Summary, Flight Info, Hotel Suggestions, Day-by-Day Itinerary, Estimated Budget, Final Recommendations.
    """
    response = llm.invoke([SystemMessage(content="You are a professional AI travel booking assistant."), HumanMessage(content=final_prompt)])
    return {
        "messages": [response],
        "llm_calls": state.get("llm_calls", 0) + 1
    }