import streamlit as st
import plotly.graph_objects as go

# Set up the Streamlit page
st.title("Interactive Sankey Diagram")

st.sidebar.header("Configure Sankey Diagram")

# Get number of nodes from the user
num_nodes = st.sidebar.number_input("Enter the number of nodes", min_value=2, max_value=20, value=5)

# Input for node names
nodes = []
for i in range(num_nodes):
    node_name = st.sidebar.text_input(f"Name for Node {i+1}", f"Node {i+1}")
    nodes.append(node_name)

# Input for links between nodes (source, target, value)
st.sidebar.subheader("Define Links")
num_links = st.sidebar.number_input("Enter the number of links", min_value=1, max_value=20, value=5)
source = []
target = []
values = []

for i in range(num_links):
    source_node = st.sidebar.selectbox(f"Source for Link {i+1}", options=list(range(num_nodes)), format_func=lambda x: nodes[x])
    target_node = st.sidebar.selectbox(f"Target for Link {i+1}", options=list(range(num_nodes)), format_func=lambda x: nodes[x])
    value = st.sidebar.number_input(f"Value for Link {i+1}", min_value=1, value=5)

    source.append(source_node)
    target.append(target_node)
    values.append(value)

# Generate Sankey Diagram
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=nodes,
        color="blue"
    ),
    link=dict(
        source=source,
        target=target,
        value=values,
        color="rgba(0, 100, 200, 0.5)"
    )
))

# Update layout
fig.update_layout(title_text="Interactive Sankey Diagram", font_size=10)

# Display the Sankey diagram
st.plotly_chart(fig)
