import { LatLngTuple } from "leaflet";

interface Word {
name: string;
origin?: string;
origin_language: Language
originMeaning?: string;
ancestors?: Word[];
comparisons?: Word[];
date?: Date
coordinates?: LatLngTuple

}


interface Language {
    name: string;
    ancestors?: Language[]
    family?: [Language]
    coordinates?: LatLngTuple
    endangerment?: string
    date?: Date
}

function Word () {


    return (
        <>
            <div>
                <p>This is the Word</p>
            </div>

        </>
    )
}

export default Word
