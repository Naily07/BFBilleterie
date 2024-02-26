import { useState } from "react";

function Dynamic(){

    const [data, setData] = useState([{fname:"", lname:""}])
 
    const handleClick=()=>{
        setData([...data,{fname:"", lname:""}])
    }
    const handleChange=()=>{

    }
    const handleDelete=()=>{

    }

    return(
        <div>
            <button onClick={handleClick}>Add</button>
            {
                data.map((val,i)=> {
                <div>
                    <input name="fname" value={val.fname} onChange={(e)=>handleChange(e,i)} />    
                    <input name="lname" value={val.fname} onChange={(e)=>handleChange(e,i)} />   
                    <button onClick={()=>handleDelete(i)}>Delete</button> 
                </div>
                })
            }

        </div>
    )
}

export default Dynamic;