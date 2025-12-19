import { useState } from "react";
import API from "../api";

function AddClient() {
  const [data, setData] = useState({
    name: "",
    description: "",
    designation: "",
    image: "",
  });

  const submit = async () => {
    await API.post("/admin/client", data);
    alert("Client Added");
    setData({ name: "", description: "", designation: "", image: "" });
  };

  return (
    <div className="card">
      <h2>Add Client</h2>

      <input
        placeholder="Client Name"
        value={data.name}
        onChange={(e) => setData({ ...data, name: e.target.value })}
      />

      <input
        placeholder="Client Description"
        value={data.description}
        onChange={(e) => setData({ ...data, description: e.target.value })}
      />

      <input
        placeholder="Designation"
        value={data.designation}
        onChange={(e) => setData({ ...data, designation: e.target.value })}
      />

      <input
        placeholder="Image URL"
        value={data.image}
        onChange={(e) => setData({ ...data, image: e.target.value })}
      />

      <button onClick={submit}>Add Client</button>
    </div>
  );
}

export default AddClient;
