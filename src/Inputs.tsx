import Collapsible from 'react-collapsible';
import './index.css';

function Inputs(){
    return (
        <div className = "Inputs">
            <Collapsible trigger="Flexion">
            <label><input type="checkbox" /> bent</label>
                <label><input type="checkbox" /> crossed</label>
                <label><input type="checkbox" /> curved</label>
                <label><input type="checkbox" /> flat</label>
                <label><input type="checkbox" /> fully closed</label>
                <label><input type="checkbox" /> fully open</label>
                <label><input type="checkbox" /> stacked</label>
                <label><input type="checkbox" /> Flexion Change </label>
            </Collapsible>
            
            <Collapsible trigger="Checkboxes">
                <label><input type="checkbox" /> arm</label>
                <label><input type="checkbox" /> body</label>
                <label><input type="checkbox" /> hand</label>
                <label><input type="checkbox" /> head</label>
                <label><input type="checkbox" /> neutral</label>
                <label><input type="checkbox" /> other</label>
            </Collapsible>
        </div>
    ); 
}

export default Inputs;