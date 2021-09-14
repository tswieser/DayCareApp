import React, { useState } from 'react'




function SchoolRoute() {
    const [name, setName] = useState("")
    const [location, setLocation] = useState("")
    const [description, setDescription] = useState("")
    const [classes, setClass] = useState([{ className: "", classDescription: "" }]);

    const handleChange = (e, index) => {
        const { name, value } = e.target;
        const list = [...classes];
        list[index][name] = value;
        setClass(list);
    }
    const handleRemoveClick = (index) => {
        const list = [...classes];
        list.splice(index, 1)
        setClass(list)
    }
    const handleAddClick = () => {
        setClass([...classes, { className: "", classDescription: "" }])
    }
    console.log(name)

    return (
        <div>
            <div className="school_reg_title">
                <h1>Register a School</h1>
            </div>
            <div className="school_form_container">
                <form>
                    <div>
                        <label htmlFor="SchoolName">School Name</label>
                        <input name="SchoolName" type="text" onChange={(e) => setName(e.target)}></input>
                    </div>
                    <div>
                        <label htmlFor="location">Location</label>
                        <input name="location" type="text" onChange={(e) => setLocation(e.target)}></input>
                    </div>
                    <div>
                        <label htmlFor="description">Description</label>
                        <input name="description" type="text" onChange={(e) => setDescription(e.target)}></input>
                    </div>
                    <label>Add A Class</label>

                    {classes.map((x, i) => {
                        console.log(x)
                        return (
                            <div>
                                <label htmlFor="className">Class Name</label>
                                <input name="className" type="text" value={x.className} onChange={(e) => handleChange(e, i)}></input>
                                <label htmlFor="classDescription">Class Ages / Description</label>
                                <input name="classDescription" type="text" value={x.classDescription} onChange={(e) => handleChange(e, i)}></input>
                                {classes.length !== 1 && <i class="fas fa-minus" onClick={handleRemoveClick} ></i>}
                                {classes.length - 1 === i && <i class="fas fa-plus" onClick={handleAddClick}></i>}

                            </div>
                        )
                    })}
                </form>
            </div>
        </div>
    )


}

export default SchoolRoute;