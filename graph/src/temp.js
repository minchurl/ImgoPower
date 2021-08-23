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
      height={700}
      margin={{ top: 60, right: 80, bottom: 60, left: 80 }}
      data={data}
      indexBy="score"
      keys={['count']}
      enableGridX="true"
      enableGridY="true"
      annotations={[
        {
          type: 'circle',
          match: { key: 'count' },
          noteX: 25, 
          nodeY: 25,
          offset: 3,
          noteTextOffset: -3,
          noteWidth: 5,
          note: 'an annotation',
          size: 40,
        }
      ]}
    />
  </div>
);

render(<App />, document.getElementById("root"));