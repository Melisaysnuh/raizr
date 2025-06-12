import { latLng } from "leaflet"
import {MapContainer, TileLayer} from "react-leaflet"
import "leaflet/dist/leaflet.css";
import '../../styles/Map.css'
import mapThemes, { getDefaultTheme, isValidTheme } from "./MapThemes";

function Map () {
    const theme = "dark";
    const validatedTheme = isValidTheme(theme) ? theme : getDefaultTheme();


    return (
        <>
            <div className="map-component">
                <MapContainer
                className="map-container"
                    center={latLng(52.4771, 13.431)}
                    zoom={2}
                    style={{ height: "60vh",
                        width: "90%",
                     }}
                >
                    {/* Tile Layer for Map Theme */}
                    {mapThemes[validatedTheme] ? (
                        <TileLayer
                            attribution="&copy; OpenStreetMap contributors"
                            url={mapThemes[validatedTheme]}
                        />
                    ) : (
                        <p style={{ color: "red" }}>Invalid map theme URL</p>
                    )}








                </MapContainer>
            </div>

        </>
    )
}

export default Map
