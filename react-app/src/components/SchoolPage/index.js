import React, { useState } from 'react'
import { postSchool } from '../../store/school'
import { postClass } from '../../store/class'
import { useDispatch } from 'react-redux'



function SchoolRoute() {
    const dispatch = useDispatch();

    const [errors, setErrors] = useState([])
    const [name, setName] = useState("")
    const [location, setLocation] = useState("")
    const [description, setDescription] = useState("")
    const [classes, setClass] = useState([{ className: "", classDescription: "" }]);

    const handleSubmit = async (e) => {
        e.preventDefault()
        const school = {
            name,
            location,
            description
        }
        const newSchool = await dispatch(postSchool(school))
        if (newSchool.errors) {
            setErrors(newSchool.errors);
            return
        }

        classes.forEach(async (c) => {
            const newClass = {
                name: c.className,
                description: c.classDescription
            }
            const resClass = await dispatch(postClass(newSchool.id, newClass))
            if (resClass.errors) {
                setErrors(resClass.errors);
                return
            }
        })
    }


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


    return (
        <div>
            <div className="school_reg_title">
                <h1>Register a School</h1>
            </div>
            <ul className="form_error_container">
                {errors &&
                    errors.map((error, i) => (
                        <li className="errors" key={i}>
                            {error}
                        </li>
                    ))}
            </ul>
            <div className="school_form_container">
                <form onSubmit={handleSubmit}>
                    <div>
                        <label htmlFor="name">School Name</label>
                        <input id="name" name="name" type="text" value={name} onChange={(e) => setName(e.target.value)}></input>
                    </div>
                    <div>
                        <label htmlFor="location">Location</label>
                        <input name="location" type="text" onChange={(e) => setLocation(e.target.value)}></input>
                    </div>
                    <div>
                        <label htmlFor="description">Description</label>
                        <input name="description" type="text" onChange={(e) => setDescription(e.target.value)}></input>
                    </div>
                    <label>Add A Class</label>

                    {classes.map((x, i) => {
                        return (
                            <div>
                                <label htmlFor="className">Class Name</label>
                                <input name="className" type="text" value={x.className} onChange={(e) => handleChange(e, i)}></input>
                                <label htmlFor="classDescription">Class Ages / Description</label>
                                <input name="classDescription" type="text" value={x.classDescription} onChange={(e) => handleChange(e, i)}></input>
                                {classes.length - 1 === i && <i class="fas fa-plus" onClick={handleAddClick}></i>}
                                {classes.length !== 1 && <i class="fas fa-minus" onClick={handleRemoveClick} ></i>}
                            </div>
                        )
                    })}
                    <div>
                        <button type="submit">Submit</button>
                    </div>
                </form>
            </div>
        </div>
    )


}

export default SchoolRoute;
