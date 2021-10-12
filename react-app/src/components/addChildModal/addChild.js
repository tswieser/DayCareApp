import React, { useState } from "react";

function AddChild({ setShowModal }) {

    const [first_name, setFirstName] = useState("")
    const [last_name, setLastName] = useState("")
    const [age, setAge] = useState("")
    const [birthday, setBirthday] = useState("")
    const [profile_img_url, setProfileImage] = useState("")
    const [notes, setNotes] = useState("")
    const [errors, setErrors] = useState("")

    const handleSubmit = async (e) => {
        e.preventDefault()

        const child = {
            first_name,
            last_name,
            age,
            birthday,
            profile_img_url,
            notes
        }
        
        console.log(child)
        setShowModal(false)
    }

    return (
        <div>
            <h1>Add Child</h1>
            <div>
                <form onSubmit={handleSubmit}>
                    <ul className="form_error_container">
                        {errors &&
                            errors.map((error, i) => (
                                <li className="errors" key={i}>
                                    {error}
                                </li>
                            ))}
                    </ul>
                    <div className="form_label_container">
                        <label htmlFor="firstName" className="form_labels">
                            First Name
                        </label>
                    </div>
                    <div>
                        <input id="firstName" className="child_input_name" name="name" type="text" value={first_name} onChange={(e) => setFirstName(e.target.value)} />
                    </div>
                    <div className="form_label_container">
                        <label htmlFor="lastName" className="form_labels">
                            Last Name
                        </label>
                    </div>
                    <div>
                        <input id="lastName" className="child_input_name" name="name" type="text" value={last_name} onChange={(e) => setLastName(e.target.value)} />
                    </div>
                    <div className="form_label_container">
                        <label htmlFor="age" className="form_labels">
                            Age
                        </label>
                    </div>
                    <div>
                        <input id="age" className="child_input_name" name="age" type="number" value={age} onChange={(e) => setAge(e.target.value)} />
                    </div>
                    <div className="form_label_container">
                        <label htmlFor="Birthday" className="form_labels">
                            Birthday
                        </label>
                    </div>
                    <div>
                        <input id="Birthday" className="child_input_name" name="Birthday" type="date" value={birthday} onChange={(e) => setBirthday(e.target.value)} />
                    </div>
                    <div className="form_label_container">
                        <label htmlFor="profile_img_url" className="form_labels">
                            Profile Image Url
                        </label>
                    </div>
                    <div>
                        <input id="profile_img_url" className="child_input_name" name="profile_img_url" type="text" value={profile_img_url} onChange={(e) => setProfileImage(e.target.value)} />
                    </div>
                    <div className="form_label_container">
                        <label htmlFor="notes" className="form_labels">
                            Notes
                        </label>
                    </div>
                    <div>
                        <textarea id="notes" className="child_input_name" name="notes" type="text" value={notes} onChange={(e) => setNotes(e.target.value)} />
                    </div>
                    <div>
                        <button type="submit">
                            Submit
                        </button>
                    </div>

                </form>

            </div>
        </div>
    )


}

export default AddChild
