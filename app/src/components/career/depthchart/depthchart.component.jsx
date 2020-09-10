import React from 'react';

import DepthChartRow from '../depthchartrow/depthchartrow.component';
import './depthchart.styles.scss';

const DepthChart = ({attackRows, midfieldRows, defenseRows, squad}) => (
    <div className="depthChart">
        <DepthChartRow slots={parseInt(attackRows)} players={squad['attack']} />
        {
         midfieldRows.map(n => (
            <DepthChartRow slots={parseInt(n)} players={squad['midfield']} />
        ))
        }
        <DepthChartRow slots={parseInt(defenseRows)} players={squad['defense']} />
        <DepthChartRow slots={1} players={squad['gk']} />
    </div>
);

export default DepthChart;