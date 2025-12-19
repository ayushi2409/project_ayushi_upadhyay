import { useState } from "react";
import API from "../api";

function AddProject() {
  const [data, setData] = useState({
    name: "",
    description: "",
    image: "",
  });

  const submit = async () => {
    await API.post("/admin/project", data);
    alert("Project Added");
    setData({ name: "", description: "", image: "" });
  };

  return (
    <div className="card">
      <h2>Add Project</h2>

      <input
        placeholder="Project Name"
        value={data.name}
        onChange={(e) => setData({ ...data, name: e.target.value })}
      />

      <input
        placeholder="Project Description"
        value={data.description}
        onChange={(e) => setData({ ...data, description: e.target.value })}
      />

      <input
        placeholder="Image URL"
        value={data.image}
        onChange={(e) => setData({ ...data, image: e.target.value })}
      />

      <button onClick={submit}>Add Project</button>
    </div>
  );
}

export default AddProject;
