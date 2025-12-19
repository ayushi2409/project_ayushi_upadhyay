import { useEffect, useState } from "react";
import API from "../api";

function Contacts() {
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    API.get("/admin/contacts").then((res) => setContacts(res.data));
  }, []);

  return (
    <div className="card">
      <h2>Contact Form Responses</h2>

      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Mobile</th>
            <th>City</th>
          </tr>
        </thead>
        <tbody>
          {contacts.map((c) => (
            <tr key={c.id}>
              <td>{c.full_name}</td>
              <td>{c.email}</td>
              <td>{c.mobile}</td>
              <td>{c.city}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Contacts;
