import React, { useEffect, useState } from "react";

interface Item {
  cd_secao: string;
  de_secao: string;
}

function App() {
  const [data, setData] = useState<Item[] | null>(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/secoes/")
      .then((response) => response.json())
      .then((data: Item[]) => setData(data))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div>
      {data
        ? data.map((item: Item) => (
            <div key={item.cd_secao}>{item.de_secao}</div>
          ))
        : "Carregando..."}
    </div>
  );
}

export default App;
