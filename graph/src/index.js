import React from "react";
import { render } from "react-dom";
import { Bar } from "@nivo/bar";


let data = require('./json/data.json')

const styles = {
  fontFamily: "sans-serif",
  textAlign: "center"
};

const myscore = 85;


const App = () => (
  <div style={styles}>
    <Bar
      width={1200}
      height={900}
      margin={{ top: 60, right: 80, bottom: 60, left: 80 }}
      data={data}
      indexBy='score'
      keys={['count']}
      enableGridX="true"
      enableGridY="true"
      annotations={[
        {
          type: 'circle',
          match: { key: 'count.82' },
          noteX: 40, 
          noteY: 40,
          offset: 1,
          offset: 3,
          note: 'an',
          size: 40,
        }
      ]}
    />
  </div>
);

render(<App />, document.getElementById("root"));