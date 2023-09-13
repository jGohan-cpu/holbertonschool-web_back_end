/*
 * The `ClassRoom` class represents a classroom.
 *
 * It has one attribute:
 *    * maxStudentsSize (Number): The maximum number of students that can be in the classroom.
 */

export default class ClassRoom {
    /*
     * Constructs a new classroom.
     *
     * Args:
     *    maxStudentsSize (Number): The maximum number of students that can be in the classroom.
     */

    constructor(maxStudentsSize) {
        /*
         * The `_maxStudentsSize` property is private, which means that it can only be accessed by the `ClassRoom` class itself.
         */
        this._maxStudentsSize = maxStudentsSize;
    }
}