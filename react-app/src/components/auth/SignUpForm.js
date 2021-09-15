import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';
import { getSchool } from '../../store/school';
import { getClass } from '../../store/class';

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [first_name, setFirstName] = useState('');
  const [last_name, setLastName] = useState('');
  const [role_cd, setRole] = useState('');
  const [school_id, setSchool] = useState('');
  const [class_id, setClass] = useState('');
  const [email, setEmail] = useState('');
  const [profile_img_url, setProfileImage] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const schools = useSelector(state => Object.values(state.schools))
  const classes = useSelector(state => Object.values(state.classes))
  const dispatch = useDispatch();

  console.log(schools)

  useEffect(() => {
    dispatch(getSchool())
  }, [dispatch])

  useEffect(() => {
    dispatch(getClass(school_id))
  }, [school_id])

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(signUp(first_name, last_name, email, password, role_cd, school_id, class_id, profile_img_url));
      if (data) {
        setErrors(data)
      }
    } else {
      setErrors(["Passwords Do not match"])
    }
  };

  if (user) {
    return <Redirect to='/' />;
  }

  return (
    <form onSubmit={onSignUp}>
      <div>
        {errors.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div>
      <div>
        <label>First Name</label>
        <input
          type='text'
          name='firstName'
          onChange={(e) => setFirstName(e.target.value)}
          value={first_name}
        ></input>
      </div>
      <div>
        <label>Last Name</label>
        <input
          type='text'
          name='lastName'
          onChange={(e) => setLastName(e.target.value)}
          value={last_name}
        ></input>
      </div>
      <div>
        <label>Email</label>
        <input
          type='text'
          name='email'
          onChange={(e) => setEmail(e.target.value)}
          value={email}
        ></input>
      </div>
      <div>
        <label>Image Url</label>
        <input
          type='text'
          name='image'
          onChange={(e) => setProfileImage(e.target.value)}
          value={profile_img_url}
        ></input>
      </div>
      <div>
        <label>Password</label>
        <input
          type='password'
          name='password'
          onChange={(e) => setPassword(e.target.value)}
          value={password}
        ></input>
      </div>
      <div>
        <label>Repeat Password</label>
        <input
          type='password'
          name='repeat_password'
          onChange={(e) => setRepeatPassword(e.target.value)}
          value={repeatPassword}
          required={true}
        ></input>
      </div>
      <div>
        <label>Select Role</label>
        <select name="role" onChange={(e) => setRole(e.target.value)}>
          <option></option>
          <option value="Parent">Parent/ Guardian</option>
          <option value="Teacher">Teacher</option>
          <option value="Admin">Admin</option>
        </select>
      </div>
      <div>
        <label>Select School</label>
        <select name="role" onChange={(e) => setSchool(e.target.value)}>
          <option>Select A School</option>
          {schools.map((school) => {
            return (
              <option value={school.id}>{school.name}</option>
            )
          })}
        </select>
      </div>
      <div>
        <label>Select Class</label>
        <select name="role" onChange={(e) => setClass(e.target.value)}>
          <option>Select A Class Room</option>
          {classes.map((allClass) => {
            return (
              <option value={allClass.id}>{allClass.name}</option>
            )
          })}

        </select>
      </div>
      <button type='submit'>Sign Up</button>
    </form >
  );
};

export default SignUpForm;
