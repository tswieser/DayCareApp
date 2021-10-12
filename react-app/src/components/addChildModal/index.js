import React, { useState } from "react";
import { Modal } from "../../context/Modal";
import AddChild from "./addChild";


function ChildModal() {
    const [showModal, setShowModal] = useState(false);

    return (
        <>
            <div className="plus_div" onClick={() => setShowModal(true)}>
                <i className="fas fa-plus fa-2x"></i>
            </div>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <AddChild setShowModal={setShowModal} />
                </Modal>
            )}
        </>
    );
}

export default ChildModal;
