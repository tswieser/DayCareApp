const GET_CLASSES = 'classes/GET_CLASSES'
const POST_CLASSES = 'classes/POST_CLASSES'

const loadClasses = (classes) => ({
    type: GET_CLASSES,
    classes
})

const createClass = (classes) => ({
    type: POST_CLASSES,
    classes
})

export const getClass = (id) => async (dispatch) => {
    const res = await fetch(`/api/class/${id}`)
    const classes = await res.json()
    if (res.ok) {
        dispatch(loadClasses(classes))
        return classes
    }
}

export const postClass = (id, classes) => async (dispatch) => {
    console.log(classes)
    const res = await fetch(`/api/class/${id}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(classes)
    })
    if (res.ok) {
        const data = await res.json();
        if (data.errors) {
            return data
        }
        dispatch(createClass(data))
        return data
    }
}


const initialState = {}

const classReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_CLASSES:
            const allClasses = {}
            action.classes.classes.forEach((classes) => {
                allClasses[classes.id] = classes
            })
            return allClasses

        case POST_CLASSES:
            return {
                ...state,
                [action.classes.id]: action.classes
            }
        default:
            return state;

    }
}

export default classReducer
