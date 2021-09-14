const GET_SCHOOLS = "schools/GET_SCHOOLS"
const POST_SCHOOLS = "schools/POST_SCHOOLS"


const loadSchools = (schools) => ({
    type: GET_SCHOOLS,
    schools
})

const createSchool = (school) => ({
    type: POST_SCHOOLS,
    school
})

export const getSchool = () => async (dispatch) => {
    const res = await fetch('api/school')
    const schools = await res.json()

    if (res.ok) {
        dispatch(loadSchools(schools))
        return schools
    }
}

export const postSchool = (school) => async (dispatch) => {
    const res = await fetch('api/school', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(school)
    })
    if (res.ok) {
        const data = await res.json()
        if (data.errors) {
            return data
        }
        dispatch(createSchool(data))
        return data
    }
}


const initialState = {}

const schoolReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_SCHOOLS:
            const all_schools = {}
            action.schools.schools.forEach((school) => {
                all_schools[school.id] = school
            })
            return all_schools

        case POST_SCHOOLS:
            return {
                ...state,
                [action.school.id]: action.school
            }
        default:
            return state;
    }

}

export default schoolReducer
