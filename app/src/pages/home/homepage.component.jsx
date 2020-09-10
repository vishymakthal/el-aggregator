import React from 'react';
import FormGroup from '@material-ui/core/FormGroup';
import Switch from '@material-ui/core/Switch';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';

import SearchBox from '../../components/searchbox/searchbox.component';

import './homepage.styles.scss';

class HomePage extends React.Component {
    
    constructor(props) {
        super(props);

        this.state = {
            index: "players",
            checkedIndex: false,
            fullSearch: false,
        }
    };
    
    toggleIndex = (event) => {
        this.setState({[event.target.name]: event.target.checked });
        this.setState(this.state.checkedIndex ? {index: "players"} : {index: "teams"})
    };

    togglePlayerSearch = (event) => {
        this.setState({[event.target.name]: event.target.checked });
    }

    render () {
        const ix = this.state.index
        return (
            <div className="homePage">
                <h1>EL AGGREGATOR</h1>
                <FormGroup>                    
                    <Typography component="div">
                        <Grid component="label" container alignItems="center" spacing={1}>
                        <Grid item>Players</Grid>
                        <Grid item>
                            <Switch checked={this.state.checkedIndex} onChange={this.toggleIndex} name="checkedIndex" />
                        </Grid>
                        <Grid item>Teams</Grid>
                        </Grid>
                    </Typography>
                    {// TODO - Get full search working
                    /* <FormControlLabel component="div"
                        control={<Switch disabled={this.state.checkedIndex} checked={this.state.fullSearch} onChange={this.togglePlayerSearch} name="fullSearch" />}
                        label="Full Search"
                    /> */}
                </FormGroup>
                <SearchBox index={ix} full={this.state.fullSearch} />
            </div>
        )
    }
}

export default HomePage;