
import React from 'react';
import { useSelector } from "react-redux";
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';

const NavBar = () => {
  const sessionUser = useSelector(state => state.session.user)




  let sessionLinks;
  if (sessionUser) {
    if (sessionUser.role_cd === 'Admin' || sessionUser.role_cd === 'Teacher') {
      sessionLinks = (
        <ul>
          <li>
            Admin/ teacher
          </li>
          <li>
            <LogoutButton />
          </li>
        </ul>
      );
    } else {
      sessionLinks = (
        <ul>
          <li>
            <NavLink to='/children' exact={true} activeClassName='active'>
              Children
            </NavLink>
          </li>
          <li>
            <LogoutButton />
          </li>
        </ul>
      );
    }
  } else {
    sessionLinks = (
      <ul>
        <li>
          <NavLink to='/login' exact={true} activeClassName='active'>
            Login
          </NavLink>
        </li>
        <li>
          <NavLink to='/sign-up' exact={true} activeClassName='active'>
            Sign Up
          </NavLink>
        </li>
        <li>
          <NavLink to='/school' exact={true} activeClassName='active'>
            School Registration
          </NavLink>
        </li>
      </ul>
    )
  }



  return (
    <nav>
      <div>
        <div>
          <NavLink to='/' exact={true} activeClassName='active'>
            Home
          </NavLink>
        </div>
        <div>
          {sessionLinks}
        </div>
      </div>
    </nav>
  );
}

export default NavBar;
