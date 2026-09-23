"""Let the model choose when to call a normal Python function."""
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

CATALOG = {"laptop stand": 34.99, "wireless mouse": 24.50, "usb-c hub": 49.00}


def get_product_price(product_name: str) -> str:
    """Return a product's current price from the demo catalog."""
    price = CATALOG.get(product_name.lower())
    return f"{product_name}: ${price:.2f}" if price else f"No product named '{product_name}' was found."


agent = Agent(
    model=Groq(id="qwen/qwen3.6-27b"),
    tools=[get_product_price],
    instructions="Use the product-price tool for price questions. Never guess a price.",
    markdown=True,
)

agent.print_response("What does the USB-C hub cost?", stream=True)
