import streamlit as st
import os

file_name = "contacts.txt"

st.title("📞 Contact Book")

menu = ["Add Contact", "View Contacts", "Search Contact", "Delete Contact"]
choice = st.sidebar.selectbox("Menu", menu)

# ADD CONTACT
if choice == "Add Contact":

    st.subheader("Add New Contact")

    name = st.text_input("Enter Name")
    phone = st.text_input("Enter Phone Number")

    if st.button("Save Contact"):

        with open(file_name, "a") as f:
            f.write(name + "," + phone + "\n")

        st.success("Contact saved successfully")


# VIEW CONTACTS
elif choice == "View Contacts":

    st.subheader("All Contacts")

    if os.path.exists(file_name):

        with open(file_name, "r") as f:
            contacts = f.readlines()

        if contacts:
            for contact in contacts:
                name, phone = contact.strip().split(",")
                st.write("Name:", name, "| Phone:", phone)
        else:
            st.warning("No contacts found")

    else:
        st.warning("No contact file found")


# SEARCH CONTACT
elif choice == "Search Contact":

    st.subheader("Search Contact")

    search_name = st.text_input("Enter Name")

    if st.button("Search"):

        found = False

        if os.path.exists(file_name):

            with open(file_name, "r") as f:
                for contact in f:
                    name, phone = contact.strip().split(",")

                    if name.lower() == search_name.lower():
                        st.success(f"Found: {name} - {phone}")
                        found = True

        if not found:
            st.error("Contact not found")


# DELETE CONTACT
elif choice == "Delete Contact":

    st.subheader("Delete Contact")

    delete_name = st.text_input("Enter Name to Delete")

    if st.button("Delete"):

        if os.path.exists(file_name):

            with open(file_name, "r") as f:
                contacts = f.readlines()

            with open(file_name, "w") as f:
                for contact in contacts:
                    name, phone = contact.strip().split(",")

                    if name.lower() != delete_name.lower():
                        f.write(contact)

            st.success("Contact deleted (if existed)")