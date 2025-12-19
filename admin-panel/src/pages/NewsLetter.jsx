import { useEffect, useState } from "react";
import API from "../api";

function Newsletter() {
  const [emails, setEmails] = useState([]);

  useEffect(() => {
    API.get("/admin/newsletter").then((res) => setEmails(res.data));
  }, []);

  return (
    <div className="card">
      <h2>Newsletter Subscribers</h2>

      <table>
        <thead>
          <tr>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {emails.map((e) => (
            <tr key={e.id}>
              <td>{e.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Newsletter;
