

let EARTH_ORBITAL_SECONDS = 31557600.0

let PLANET_YEAR_RATIO = [
    "mercury": 0.2408467,
    "venus": 0.61519726,
    "earth": 1.0,
    "mars": 1.8808158,
    "jupiter": 11.862615,
    "saturn": 29.447498,
    "uranus": 84.016846,
    "neptune": 164.79132,
]


class SpaceAge {
    let seconds :Int

    init(_ _seconds: Int) {
        seconds = _seconds
    }

    private var _earthYears: Double {
        return Double(seconds) / EARTH_ORBITAL_SECONDS
    }

    private func on(planet: String) -> Double {
        let years = _earthYears / PLANET_YEAR_RATIO[planet.lowercased()]!
        return (years * 100).rounded() / 100
    }

    var onEarth: Double {
        return on(planet: "earth")
    }

    var onMercury: Double {
        return on(planet: "mercury")
    }

    var onVenus: Double {
        return on(planet: "venus")
    }

    var onMars: Double {
        return on(planet: "mars")
    }

    var onJupiter: Double {
        return on(planet: "jupiter")
    }

    var onSaturn: Double {
        return on(planet: "saturn")
    }

    var onUranus: Double {
        return on(planet: "uranus")
    }

    var onNeptune: Double {
        return on(planet: "neptune")
    }
}