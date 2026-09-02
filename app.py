import streamlit as st

from agents.commerce_agent import CommerceAgent


st.set_page_config(
    page_title="Vendora AI",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Vendora AI")
st.caption("AI-Powered Agentic Commerce")

if "agent" not in st.session_state:
    st.session_state.agent = CommerceAgent()

if "result" not in st.session_state:
    st.session_state.result = None


user_message = st.chat_input(
    "What are you looking for?"
)


if user_message:

    with st.chat_message("user"):
        st.write(user_message)

    result = st.session_state.agent.process_request(
        user_message
    )

    st.session_state.result = result


if st.session_state.result:

    result = st.session_state.result

    if not result["success"]:

        st.error(result["message"])

    else:

        product = result["product"]
        suggestions = result["suggestions"]

        with st.chat_message("assistant"):

            st.success("I found a suitable product for you!")

            st.subheader(product["product_name"])

            st.write(product["description"])

            st.write(f"💰 **Price:** ₹{product['price']}")
            st.write(f"⭐ **Rating:** {product['rating']}")

            st.divider()

            st.subheader("💡 Smart Recommendations")

            if suggestions["upsell"]:

                item = suggestions["upsell"]

                st.info(
                    f"⬆️ **Upgrade:** {item['product_name']} "
                    f"— ₹{item['price']}"
                )

                if st.button(
                    f"Add {item['product_name']}",
                    key="add_upsell"
                ):
                    cart_result = st.session_state.agent.add_product(
                        item
                    )

                    st.success("Added to cart!")
                    st.rerun()

            if suggestions["cross_sell"]:

                item = suggestions["cross_sell"]

                st.info(
                    f"➕ **Also useful:** {item['product_name']} "
                    f"— ₹{item['price']}"
                )

                if st.button(
                    f"Add {item['product_name']}",
                    key="add_cross_sell"
                ):
                    cart_result = st.session_state.agent.add_product(
                        item
                    )

                    st.success("Added to cart!")
                    st.rerun()


# -------------------------
# Cart
# -------------------------

st.sidebar.title("🛒 Your Cart")

cart_items = st.session_state.agent.cart.get_items()

if cart_items:

    for item in cart_items:

        st.sidebar.write(
            f"**{item['product_name']}**"
        )

        st.sidebar.write(
            f"₹{item['price']}"
        )

        st.sidebar.divider()

    total = st.session_state.agent.cart.get_total()

    st.sidebar.subheader(
        f"Total: ₹{total}"
    )

else:

    st.sidebar.info("Your cart is empty.")