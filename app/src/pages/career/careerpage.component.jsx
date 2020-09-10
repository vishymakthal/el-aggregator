import React from 'react';
import DepthChart from '../../components/career/depthchart/depthchart.component';
import FormationSelector from '../../components/career/formationselector/formationselector.component';

class CareerPage extends React.Component {
    constructor () {
        super();

        this.state = {
            currentFormation :  "4-3-3",
            squad : {}
        }
    }

    async componentDidMount () {
        fetch('https://el-aggregator-api-q3hl2qd3ia-uk.a.run.app/api/v1/players/team/979786270', {method: 'GET'})
        .then(response => response.json())
        .then(players => this.setState({squad : players}))
    }
    
    render() {
       
        const formationRows = this.state.currentFormation.split('-')
        const defense = formationRows[0]
        const midfield = formationRows.slice(1,formationRows.length - 1)
        const attack = formationRows[formationRows.length - 1]
        return(
            <div className="careerPage">
                <h1>Career Mode Hub</h1>
                <FormationSelector  handler={e => this.setState({currentFormation : e.target.value}, () => console.log())} />
                <DepthChart attackRows={attack} midfieldRows={midfield} defenseRows={defense} squad={this.state.squad}/>
            </div>
        )
    }
}

export default CareerPage;