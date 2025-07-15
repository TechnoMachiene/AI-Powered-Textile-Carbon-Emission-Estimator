from flask import Flask, request, jsonify

app = Flask(__name__)

# Your emission dataset
emission_data = {
    "materials": {
        "Cotton": 3.61,
        "Polyester (virgin)": 3.12,
        "Polyester (mechanically recycled)": 1.12, 
        "Wool": 46.0,
        "Silk": 25.0,
        "Acrylic": 38.0,
        "Linen / Flax": 15.0
    },
    "manufacturing_processes": {
        "Spinning & Weaving": 1.25,
        "Dyeing & Finishing": 3.0,
        "Garment Assembly": 0.6,
        "Leather Tanning": 22.5,   
        "Cotton Fabric (Dyed)": 10.8
    },
    "origin_multipliers": {
        "Bangladesh": 1.35,
        "India": 1.25,
        "China": 1.15,
        "Turkey": 1.0,
        "EU / US":  0.9
    },
    "transport_modes": {
        "Road": 0.09,
        "Rail": 0.03,
        "Sea Freight": 0.025,
        "Air Cargo": 0.75
    }
}

@app.route('/calculate_co2e', methods=['POST'])
def calculate_co2e():
    data = request.get_json()

    try:
        # Extract inputs
        material = data['material']
        processes = data['manufacturing_processes']  # list
        origin = data['origin']
        transport_mode = data['transport_mode']
        weight = float(data['weight'])  # in kg
        distance = float(data['distance'])  # in km

        # Validate material
        material_co2e = emission_data["materials"].get(material)
        if material_co2e is None:
            return jsonify({"error": f"Unknown material: {material}"}), 400

        # Sum manufacturing multipliers
        total_process_multiplier = 0.0
        for process in processes:
            multiplier = emission_data["manufacturing_processes"].get(process)
            if multiplier is None:
                return jsonify({"error": f"Unknown manufacturing process: {process}"}), 400
            total_process_multiplier += multiplier

        # Get origin multiplier
        origin_multiplier = emission_data["origin_multipliers"].get(origin)
        if origin_multiplier is None:
            return jsonify({"error": f"Unknown origin: {origin}"}), 400

        # Get transport emission factor
        transport_factor = emission_data["transport_modes"].get(transport_mode)
        if transport_factor is None:
            return jsonify({"error": f"Unknown transport mode: {transport_mode}"}), 400

        # CO2e Calculation
        base_emissions = material_co2e + (material_co2e * total_process_multiplier)
        total_emissions = (base_emissions * origin_multiplier) + (weight * distance * transport_factor)

        return jsonify({
            "material": material,
            "processes": processes,
            "origin": origin,
            "transport_mode": transport_mode,
            "weight": weight,
            "distance": distance,
            "total_co2e_kg": round(total_emissions, 4)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
