import React, { useState } from 'react'




function SchoolRoute() {
    const [name, setName] = useState("")
    const [location, setLocation] = useState("")
    const [description, setDescription] = useState("")

    return (
        <div>
            <div className="school_reg_title">
                <h1>Register a School</h1>
            </div>
            <div className="school_form_container">
                <form>
                    <div>
                        <label htmlFor="SchoolName">School Name</label>
                        <input name="SchoolName" type="text" value={name} onChange={(e) => setName(e.target)}></input>
                    </div>
                    <div>
                        <label htmlFor="location">Location</label>
                        <input name="location" type="text" value={location} onChange={(e) => setLocation(e.target)}></input>
                    </div>
                    <div>
                        <label htmlFor="description">Description</label>
                        <input name="description" type="text" value={description} onChange={(e) => setDescription(e.target)}></input>
                    </div>
                </form>
            </div>
        </div>
    )


}

export default SchoolRoute;
