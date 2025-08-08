import streamlit as st
def detect_language(text):
    # Simple language detection based on common Spanish words
    spanish_words = ['hola', 'como', 'que', 'por', 'para', 'con', 'una', 'una', 'del', 'las', 'los', 'el', 'la']
    text_lower = text.lower()
    spanish_count = sum(1 for word in spanish_words if word in text_lower)
    return 'es' if spanish_count > 0 else 'en'
import datetime

# Your knowledge base (same as before)
business_knowledge = {
    "return": {
        "en": "Items can be returned within 30 days with original receipt. Refunds processed in 3-5 business days.",
        "es": "Los artículos se pueden devolver dentro de 30 días con recibo original. Reembolsos procesados en 3-5 días hábiles."
    },
    "shipping": {
        "en": "Standard shipping takes 3-5 business days and costs $5.99. Free shipping on orders over $50. Express shipping available for $12.99.",
        "es": "El envío estándar toma 3-5 días hábiles y cuesta $5.99. Envío gratis en pedidos sobre $50. Envío express disponible por $12.99."
    },
    "hours": {
        "en": "Store hours: Monday-Friday 9AM-8PM, Saturday-Sunday 10AM-6PM. Holiday hours may vary.",
        "es": "Horarios de tienda: Lunes-Viernes 9AM-8PM, Sábado-Domingo 10AM-6PM. Los horarios de feriados pueden variar."
    },
    "contact": {
        "en": "Contact us: Phone (555) 123-4567, Email support@yourstore.com, or chat online 24/7.",
        "es": "Contáctanos: Teléfono (555) 123-4567, Email support@yourstore.com, o chat en línea 24/7."
    }
}

def detect_language(text):
    try:
        return detect(text)
    except:
        return 'en'

def find_best_answer(question, language):
    question = question.lower()
    
    if any(word in question for word in ["return", "refund", "devolver", "reembolso"]):
        return business_knowledge["return"][language]
    elif any(word in question for word in ["shipping", "delivery", "envío", "entrega"]):
        return business_knowledge["shipping"][language]
    elif any(word in question for word in ["hours", "open", "close", "horario", "abierto"]):
        return business_knowledge["hours"][language]
    elif any(word in question for word in ["contact", "phone", "email", "contacto", "teléfono"]):
        return business_knowledge["contact"][language]
    elif any(word in question for word in ["hello", "hi", "hola"]):
        if language == 'es':
            return "¡Hola! Soy tu asistente de servicio al cliente. ¿Cómo puedo ayudarte hoy?"
        else:
            return "Hello! I'm your customer service assistant. How can I help you today?"
    else:
        if language == 'es':
            return "Puedes preguntar sobre devoluciones, envíos, horarios, o contacto. ¿En qué más puedo ayudarte?"
        else:
            return "You can ask about returns, shipping, hours, or contact info. How else can I help?"

# Streamlit App
st.set_page_config(
    page_title="Customer Support Chat",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Customer Support Assistant")
st.subheader("🌍 English & Spanish Support | Soporte en Inglés y Español")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything... Pregúntame cualquier cosa..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    language = detect_language(prompt)
    response = find_best_answer(prompt, language)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

# Sidebar with info
st.sidebar.title("📋 Quick Help")
st.sidebar.markdown("""
**English:**
- Returns & Refunds
- Shipping Information
- Store Hours
- Contact Information

**Español:**
- Devoluciones y Reembolsos
- Información de Envío
- Horarios de Tienda
- Información de Contacto
""")

st.sidebar.markdown("---")

st.sidebar.markdown("💡 **Tip:** Ask questions naturally in English or Spanish!")
