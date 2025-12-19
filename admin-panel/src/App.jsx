import AddProject from "./pages/AddProject";
import AddClient from "./pages/AddClient";
import Contacts from "./pages/Contacts";
import Newsletter from "./pages/Newsletter";
import "./index.css";

function App() {
  return (
    <div className="container">
      <h1>Admin Panel</h1>

      <AddProject />
      <AddClient />
      <Contacts />
      <Newsletter />
    </div>
  );
}

export default App;
