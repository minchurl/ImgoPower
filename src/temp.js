import React from "react";
import { render } from "react-dom";
import { Bar } from "@nivo/bar";

const styles = {
  fontFamily: "sans-serif",
  textAlign: "center"
};

const App = () => (
  <div style={styles}>
    <Bar
      width={600}
      height={400}
      margin={{ top: 60, right: 80, bottom: 60, left: 80 }}
      data={[
        { country: "AD", "hot dogs": 13 },
        { country: "AE", "hot dogs": 7 },
        { country: "AF", "hot dogs": 9 }
      ]}
      indexBy="country"
      keys={["hot dogs"]}
    />
  </div>
);

render(<App />, document.getElementById("root"));
