# -*- coding: utf-8 -*-
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

CAR_CATEGORIES = [
	{"color": [0, 0, 255], "isthing": 1, "id": 1, "name": "AM General Hummer SUV 2000"},
	{"color": [0, 0, 255], "isthing": 1, "id": 2, "name": "Acura RL Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 3, "name": "Acura TL Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 4, "name": "Acura TL Type-S 2008"},
	{"color": [0, 0, 255], "isthing": 1, "id": 5, "name": "Acura TSX Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 6, "name": "Acura Integra Type R 2001"},
	{"color": [0, 0, 255], "isthing": 1, "id": 7, "name": "Acura ZDX Hatchback 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 8, "name": "Aston Martin V8 Vantage Convertible 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 9, "name": "Aston Martin V8 Vantage Coupe 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 10, "name": "Aston Martin Virage Convertible 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 11, "name": "Aston Martin Virage Coupe 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 12, "name": "Audi RS 4 Convertible 2008"},
	{"color": [0, 0, 255], "isthing": 1, "id": 13, "name": "Audi A5 Coupe 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 14, "name": "Audi TTS Coupe 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 15, "name": "Audi R8 Coupe 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 16, "name": "Audi V8 Sedan 1994"},
	{"color": [0, 0, 255], "isthing": 1, "id": 17, "name": "Audi 100 Sedan 1994"},
	{"color": [0, 0, 255], "isthing": 1, "id": 18, "name": "Audi 100 Wagon 1994"},
	{"color": [0, 0, 255], "isthing": 1, "id": 19, "name": "Audi TT Hatchback 2011"},
	{"color": [0, 0, 255], "isthing": 1, "id": 20, "name": "Audi S6 Sedan 2011"},
	{"color": [0, 0, 255], "isthing": 1, "id": 21, "name": "Audi S5 Convertible 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 22, "name": "Audi S5 Coupe 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 23, "name": "Audi S4 Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 24, "name": "Audi S4 Sedan 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 25, "name": "Audi TT RS Coupe 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 26, "name": "BMW ActiveHybrid 5 Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 27, "name": "BMW 1 Series Convertible 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 28, "name": "BMW 1 Series Coupe 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 29, "name": "BMW 3 Series Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 30, "name": "BMW 3 Series Wagon 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 31, "name": "BMW 6 Series Convertible 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 32, "name": "BMW X5 SUV 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 33, "name": "BMW X6 SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 34, "name": "BMW M3 Coupe 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 35, "name": "BMW M5 Sedan 2010"},
	{"color": [0, 0, 255], "isthing": 1, "id": 36, "name": "BMW M6 Convertible 2010"},
	{"color": [0, 0, 255], "isthing": 1, "id": 37, "name": "BMW X3 SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 38, "name": "BMW Z4 Convertible 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 39, "name": "Bentley Continental Supersports Conv. Convertible 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 40, "name": "Bentley Arnage Sedan 2009"},
	{"color": [0, 0, 255], "isthing": 1, "id": 41, "name": "Bentley Mulsanne Sedan 2011"},
	{"color": [0, 0, 255], "isthing": 1, "id": 42, "name": "Bentley Continental GT Coupe 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 43, "name": "Bentley Continental GT Coupe 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 44, "name": "Bentley Continental Flying Spur Sedan 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 45, "name": "Bugatti Veyron 16.4 Convertible 2009"},
	{"color": [0, 0, 255], "isthing": 1, "id": 46, "name": "Bugatti Veyron 16.4 Coupe 2009"},
	{"color": [0, 0, 255], "isthing": 1, "id": 47, "name": "Buick Regal GS 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 48, "name": "Buick Rainier SUV 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 49, "name": "Buick Verano Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 50, "name": "Buick Enclave SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 51, "name": "Cadillac CTS-V Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 52, "name": "Cadillac SRX SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 53, "name": "Cadillac Escalade EXT Crew Cab 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 54, "name": "Chevrolet Silverado 1500 Hybrid Crew Cab 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 55, "name": "Chevrolet Corvette Convertible 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 56, "name": "Chevrolet Corvette ZR1 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 57, "name": "Chevrolet Corvette Ron Fellows Edition Z06 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 58, "name": "Chevrolet Traverse SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 59, "name": "Chevrolet Camaro Convertible 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 60, "name": "Chevrolet HHR SS 2010"},
	{"color": [0, 0, 255], "isthing": 1, "id": 61, "name": "Chevrolet Impala Sedan 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 62, "name": "Chevrolet Tahoe Hybrid SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 63, "name": "Chevrolet Sonic Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 64, "name": "Chevrolet Express Cargo Van 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 65, "name": "Chevrolet Avalanche Crew Cab 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 66, "name": "Chevrolet Cobalt SS 2010"},
	{"color": [0, 0, 255], "isthing": 1, "id": 67, "name": "Chevrolet Malibu Hybrid Sedan 2010"},
	{"color": [0, 0, 255], "isthing": 1, "id": 68, "name": "Chevrolet TrailBlazer SS 2009"},
	{"color": [0, 0, 255], "isthing": 1, "id": 69, "name": "Chevrolet Silverado 2500HD Regular Cab 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 70, "name": "Chevrolet Silverado 1500 Classic Extended Cab 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 71, "name": "Chevrolet Express Van 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 72, "name": "Chevrolet Monte Carlo Coupe 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 73, "name": "Chevrolet Malibu Sedan 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 74, "name": "Chevrolet Silverado 1500 Extended Cab 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 75, "name": "Chevrolet Silverado 1500 Regular Cab 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 76, "name": "Chrysler Aspen SUV 2009"},
	{"color": [0, 0, 255], "isthing": 1, "id": 77, "name": "Chrysler Sebring Convertible 2010"},
	{"color": [0, 0, 255], "isthing": 1, "id": 78, "name": "Chrysler Town and Country Minivan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 79, "name": "Chrysler 300 SRT-8 2010"},
	{"color": [0, 0, 255], "isthing": 1, "id": 80, "name": "Chrysler Crossfire Convertible 2008"},
	{"color": [0, 0, 255], "isthing": 1, "id": 81, "name": "Chrysler PT Cruiser Convertible 2008"},
	{"color": [0, 0, 255], "isthing": 1, "id": 82, "name": "Daewoo Nubira Wagon 2002"},
	{"color": [0, 0, 255], "isthing": 1, "id": 83, "name": "Dodge Caliber Wagon 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 84, "name": "Dodge Caliber Wagon 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 85, "name": "Dodge Caravan Minivan 1997"},
	{"color": [0, 0, 255], "isthing": 1, "id": 86, "name": "Dodge Ram Pickup 3500 Crew Cab 2010"},
	{"color": [0, 0, 255], "isthing": 1, "id": 87, "name": "Dodge Ram Pickup 3500 Quad Cab 2009"},
	{"color": [0, 0, 255], "isthing": 1, "id": 88, "name": "Dodge Sprinter Cargo Van 2009"},
	{"color": [0, 0, 255], "isthing": 1, "id": 89, "name": "Dodge Journey SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 90, "name": "Dodge Dakota Crew Cab 2010"},
	{"color": [0, 0, 255], "isthing": 1, "id": 91, "name": "Dodge Dakota Club Cab 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 92, "name": "Dodge Magnum Wagon 2008"},
	{"color": [0, 0, 255], "isthing": 1, "id": 93, "name": "Dodge Challenger SRT8 2011"},
	{"color": [0, 0, 255], "isthing": 1, "id": 94, "name": "Dodge Durango SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 95, "name": "Dodge Durango SUV 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 96, "name": "Dodge Charger Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 97, "name": "Dodge Charger SRT-8 2009"},
	{"color": [0, 0, 255], "isthing": 1, "id": 98, "name": "Eagle Talon Hatchback 1998"},
	{"color": [0, 0, 255], "isthing": 1, "id": 99, "name": "FIAT 500 Abarth 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 100, "name": "FIAT 500 Convertible 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 101, "name": "Ferrari FF Coupe 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 102, "name": "Ferrari California Convertible 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 103, "name": "Ferrari 458 Italia Convertible 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 104, "name": "Ferrari 458 Italia Coupe 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 105, "name": "Fisker Karma Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 106, "name": "Ford F-450 Super Duty Crew Cab 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 107, "name": "Ford Mustang Convertible 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 108, "name": "Ford Freestar Minivan 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 109, "name": "Ford Expedition EL SUV 2009"},
	{"color": [0, 0, 255], "isthing": 1, "id": 110, "name": "Ford Edge SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 111, "name": "Ford Ranger SuperCab 2011"},
	{"color": [0, 0, 255], "isthing": 1, "id": 112, "name": "Ford GT Coupe 2006"},
	{"color": [0, 0, 255], "isthing": 1, "id": 113, "name": "Ford F-150 Regular Cab 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 114, "name": "Ford F-150 Regular Cab 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 115, "name": "Ford Focus Sedan 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 116, "name": "Ford E-Series Wagon Van 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 117, "name": "Ford Fiesta Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 118, "name": "GMC Terrain SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 119, "name": "GMC Savana Van 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 120, "name": "GMC Yukon Hybrid SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 121, "name": "GMC Acadia SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 122, "name": "GMC Canyon Extended Cab 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 123, "name": "Geo Metro Convertible 1993"},
	{"color": [0, 0, 255], "isthing": 1, "id": 124, "name": "HUMMER H3T Crew Cab 2010"},
	{"color": [0, 0, 255], "isthing": 1, "id": 125, "name": "HUMMER H2 SUT Crew Cab 2009"},
	{"color": [0, 0, 255], "isthing": 1, "id": 126, "name": "Honda Odyssey Minivan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 127, "name": "Honda Odyssey Minivan 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 128, "name": "Honda Accord Coupe 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 129, "name": "Honda Accord Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 130, "name": "Hyundai Veloster Hatchback 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 131, "name": "Hyundai Santa Fe SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 132, "name": "Hyundai Tucson SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 133, "name": "Hyundai Veracruz SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 134, "name": "Hyundai Sonata Hybrid Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 135, "name": "Hyundai Elantra Sedan 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 136, "name": "Hyundai Accent Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 137, "name": "Hyundai Genesis Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 138, "name": "Hyundai Sonata Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 139, "name": "Hyundai Elantra Touring Hatchback 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 140, "name": "Hyundai Azera Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 141, "name": "Infiniti G Coupe IPL 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 142, "name": "Infiniti QX56 SUV 2011"},
	{"color": [0, 0, 255], "isthing": 1, "id": 143, "name": "Isuzu Ascender SUV 2008"},
	{"color": [0, 0, 255], "isthing": 1, "id": 144, "name": "Jaguar XK XKR 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 145, "name": "Jeep Patriot SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 146, "name": "Jeep Wrangler SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 147, "name": "Jeep Liberty SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 148, "name": "Jeep Grand Cherokee SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 149, "name": "Jeep Compass SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 150, "name": "Lamborghini Reventon Coupe 2008"},
	{"color": [0, 0, 255], "isthing": 1, "id": 151, "name": "Lamborghini Aventador Coupe 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 152, "name": "Lamborghini Gallardo LP 570-4 Superleggera 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 153, "name": "Lamborghini Diablo Coupe 2001"},
	{"color": [0, 0, 255], "isthing": 1, "id": 154, "name": "Land Rover Range Rover SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 155, "name": "Land Rover LR2 SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 156, "name": "Lincoln Town Car Sedan 2011"},
	{"color": [0, 0, 255], "isthing": 1, "id": 157, "name": "MINI Cooper Roadster Convertible 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 158, "name": "Maybach Landaulet Convertible 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 159, "name": "Mazda Tribute SUV 2011"},
	{"color": [0, 0, 255], "isthing": 1, "id": 160, "name": "McLaren MP4-12C Coupe 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 161, "name": "Mercedes-Benz 300-Class Convertible 1993"},
	{"color": [0, 0, 255], "isthing": 1, "id": 162, "name": "Mercedes-Benz C-Class Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 163, "name": "Mercedes-Benz SL-Class Coupe 2009"},
	{"color": [0, 0, 255], "isthing": 1, "id": 164, "name": "Mercedes-Benz E-Class Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 165, "name": "Mercedes-Benz S-Class Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 166, "name": "Mercedes-Benz Sprinter Van 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 167, "name": "Mitsubishi Lancer Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 168, "name": "Nissan Leaf Hatchback 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 169, "name": "Nissan NV Passenger Van 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 170, "name": "Nissan Juke Hatchback 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 171, "name": "Nissan 240SX Coupe 1998"},
	{"color": [0, 0, 255], "isthing": 1, "id": 172, "name": "Plymouth Neon Coupe 1999"},
	{"color": [0, 0, 255], "isthing": 1, "id": 173, "name": "Porsche Panamera Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 174, "name": "Ram C/V Cargo Van Minivan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 175, "name": "Rolls-Royce Phantom Drophead Coupe Convertible 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 176, "name": "Rolls-Royce Ghost Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 177, "name": "Rolls-Royce Phantom Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 178, "name": "Scion xD Hatchback 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 179, "name": "Spyker C8 Convertible 2009"},
	{"color": [0, 0, 255], "isthing": 1, "id": 180, "name": "Spyker C8 Coupe 2009"},
	{"color": [0, 0, 255], "isthing": 1, "id": 181, "name": "Suzuki Aerio Sedan 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 182, "name": "Suzuki Kizashi Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 183, "name": "Suzuki SX4 Hatchback 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 184, "name": "Suzuki SX4 Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 185, "name": "Tesla Model S Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 186, "name": "Toyota Sequoia SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 187, "name": "Toyota Camry Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 188, "name": "Toyota Corolla Sedan 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 189, "name": "Toyota 4Runner SUV 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 190, "name": "Volkswagen Golf Hatchback 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 191, "name": "Volkswagen Golf Hatchback 1991"},
	{"color": [0, 0, 255], "isthing": 1, "id": 192, "name": "Volkswagen Beetle Hatchback 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 193, "name": "Volvo C30 Hatchback 2012"},
	{"color": [0, 0, 255], "isthing": 1, "id": 194, "name": "Volvo 240 Sedan 1993"},
	{"color": [0, 0, 255], "isthing": 1, "id": 195, "name": "Volvo XC90 SUV 2007"},
	{"color": [0, 0, 255], "isthing": 1, "id": 196, "name": "smart fortwo Convertible 2012"},
]    

PHONE_CATEGORIES = [
    {"color": [220, 20, 60], "isthing": 1, "id": 1, "name": "LitPhone"},
    {"color": [119, 11, 32], "isthing": 1, "id": 2, "name": "UnlitPhone"},
    {"color": [0, 0, 142], "isthing": 1, "id": 3, "name": "BackPhone"},
]



DAMAGE_CATEGORIES = [
    {"color": [220, 20, 60], "isthing": 1, "id": 1, "name": "Crack"},
    {"color": [119, 11, 32], "isthing": 1, "id": 2, "name": "Broken"},
    {"color": [0, 0, 142], "isthing": 1, "id": 3, "name": "Reflection"},
    {"color": [0, 0, 230], "isthing": 1, "id": 4, "name": "Scratch"},
]

# All coco categories, together with their nice-looking visualization colors
# It's from https://github.com/cocodataset/panopticapi/blob/master/panoptic_coco_categories.json
COCO_CATEGORIES = [
    {"color": [220, 20, 60], "isthing": 1, "id": 1, "name": "person"},
    {"color": [119, 11, 32], "isthing": 1, "id": 2, "name": "bicycle"},
    {"color": [0, 0, 142], "isthing": 1, "id": 3, "name": "car"},
    {"color": [0, 0, 230], "isthing": 1, "id": 4, "name": "motorcycle"},
    {"color": [106, 0, 228], "isthing": 1, "id": 5, "name": "airplane"},
    {"color": [0, 60, 100], "isthing": 1, "id": 6, "name": "bus"},
    {"color": [0, 80, 100], "isthing": 1, "id": 7, "name": "train"},
    {"color": [0, 0, 70], "isthing": 1, "id": 8, "name": "truck"},
    {"color": [0, 0, 192], "isthing": 1, "id": 9, "name": "boat"},
    {"color": [250, 170, 30], "isthing": 1, "id": 10, "name": "traffic light"},
    {"color": [100, 170, 30], "isthing": 1, "id": 11, "name": "fire hydrant"},
    {"color": [220, 220, 0], "isthing": 1, "id": 13, "name": "stop sign"},
    {"color": [175, 116, 175], "isthing": 1, "id": 14, "name": "parking meter"},
    {"color": [250, 0, 30], "isthing": 1, "id": 15, "name": "bench"},
    {"color": [165, 42, 42], "isthing": 1, "id": 16, "name": "bird"},
    {"color": [255, 77, 255], "isthing": 1, "id": 17, "name": "cat"},
    {"color": [0, 226, 252], "isthing": 1, "id": 18, "name": "dog"},
    {"color": [182, 182, 255], "isthing": 1, "id": 19, "name": "horse"},
    {"color": [0, 82, 0], "isthing": 1, "id": 20, "name": "sheep"},
    {"color": [120, 166, 157], "isthing": 1, "id": 21, "name": "cow"},
    {"color": [110, 76, 0], "isthing": 1, "id": 22, "name": "elephant"},
    {"color": [174, 57, 255], "isthing": 1, "id": 23, "name": "bear"},
    {"color": [199, 100, 0], "isthing": 1, "id": 24, "name": "zebra"},
    {"color": [72, 0, 118], "isthing": 1, "id": 25, "name": "giraffe"},
    {"color": [255, 179, 240], "isthing": 1, "id": 27, "name": "backpack"},
    {"color": [0, 125, 92], "isthing": 1, "id": 28, "name": "umbrella"},
    {"color": [209, 0, 151], "isthing": 1, "id": 31, "name": "handbag"},
    {"color": [188, 208, 182], "isthing": 1, "id": 32, "name": "tie"},
    {"color": [0, 220, 176], "isthing": 1, "id": 33, "name": "suitcase"},
    {"color": [255, 99, 164], "isthing": 1, "id": 34, "name": "frisbee"},
    {"color": [92, 0, 73], "isthing": 1, "id": 35, "name": "skis"},
    {"color": [133, 129, 255], "isthing": 1, "id": 36, "name": "snowboard"},
    {"color": [78, 180, 255], "isthing": 1, "id": 37, "name": "sports ball"},
    {"color": [0, 228, 0], "isthing": 1, "id": 38, "name": "kite"},
    {"color": [174, 255, 243], "isthing": 1, "id": 39, "name": "baseball bat"},
    {"color": [45, 89, 255], "isthing": 1, "id": 40, "name": "baseball glove"},
    {"color": [134, 134, 103], "isthing": 1, "id": 41, "name": "skateboard"},
    {"color": [145, 148, 174], "isthing": 1, "id": 42, "name": "surfboard"},
    {"color": [255, 208, 186], "isthing": 1, "id": 43, "name": "tennis racket"},
    {"color": [197, 226, 255], "isthing": 1, "id": 44, "name": "bottle"},
    {"color": [171, 134, 1], "isthing": 1, "id": 46, "name": "wine glass"},
    {"color": [109, 63, 54], "isthing": 1, "id": 47, "name": "cup"},
    {"color": [207, 138, 255], "isthing": 1, "id": 48, "name": "fork"},
    {"color": [151, 0, 95], "isthing": 1, "id": 49, "name": "knife"},
    {"color": [9, 80, 61], "isthing": 1, "id": 50, "name": "spoon"},
    {"color": [84, 105, 51], "isthing": 1, "id": 51, "name": "bowl"},
    {"color": [74, 65, 105], "isthing": 1, "id": 52, "name": "banana"},
    {"color": [166, 196, 102], "isthing": 1, "id": 53, "name": "apple"},
    {"color": [208, 195, 210], "isthing": 1, "id": 54, "name": "sandwich"},
    {"color": [255, 109, 65], "isthing": 1, "id": 55, "name": "orange"},
    {"color": [0, 143, 149], "isthing": 1, "id": 56, "name": "broccoli"},
    {"color": [179, 0, 194], "isthing": 1, "id": 57, "name": "carrot"},
    {"color": [209, 99, 106], "isthing": 1, "id": 58, "name": "hot dog"},
    {"color": [5, 121, 0], "isthing": 1, "id": 59, "name": "pizza"},
    {"color": [227, 255, 205], "isthing": 1, "id": 60, "name": "donut"},
    {"color": [147, 186, 208], "isthing": 1, "id": 61, "name": "cake"},
    {"color": [153, 69, 1], "isthing": 1, "id": 62, "name": "chair"},
    {"color": [3, 95, 161], "isthing": 1, "id": 63, "name": "couch"},
    {"color": [163, 255, 0], "isthing": 1, "id": 64, "name": "potted plant"},
    {"color": [119, 0, 170], "isthing": 1, "id": 65, "name": "bed"},
    {"color": [0, 182, 199], "isthing": 1, "id": 67, "name": "dining table"},
    {"color": [0, 165, 120], "isthing": 1, "id": 70, "name": "toilet"},
    {"color": [183, 130, 88], "isthing": 1, "id": 72, "name": "tv"},
    {"color": [95, 32, 0], "isthing": 1, "id": 73, "name": "laptop"},
    {"color": [130, 114, 135], "isthing": 1, "id": 74, "name": "mouse"},
    {"color": [110, 129, 133], "isthing": 1, "id": 75, "name": "remote"},
    {"color": [166, 74, 118], "isthing": 1, "id": 76, "name": "keyboard"},
    {"color": [219, 142, 185], "isthing": 1, "id": 77, "name": "cell phone"},
    {"color": [79, 210, 114], "isthing": 1, "id": 78, "name": "microwave"},
    {"color": [178, 90, 62], "isthing": 1, "id": 79, "name": "oven"},
    {"color": [65, 70, 15], "isthing": 1, "id": 80, "name": "toaster"},
    {"color": [127, 167, 115], "isthing": 1, "id": 81, "name": "sink"},
    {"color": [59, 105, 106], "isthing": 1, "id": 82, "name": "refrigerator"},
    {"color": [142, 108, 45], "isthing": 1, "id": 84, "name": "book"},
    {"color": [196, 172, 0], "isthing": 1, "id": 85, "name": "clock"},
    {"color": [95, 54, 80], "isthing": 1, "id": 86, "name": "vase"},
    {"color": [128, 76, 255], "isthing": 1, "id": 87, "name": "scissors"},
    {"color": [201, 57, 1], "isthing": 1, "id": 88, "name": "teddy bear"},
    {"color": [246, 0, 122], "isthing": 1, "id": 89, "name": "hair drier"},
    {"color": [191, 162, 208], "isthing": 1, "id": 90, "name": "toothbrush"},
    {"color": [255, 255, 128], "isthing": 0, "id": 92, "name": "banner"},
    {"color": [147, 211, 203], "isthing": 0, "id": 93, "name": "blanket"},
    {"color": [150, 100, 100], "isthing": 0, "id": 95, "name": "bridge"},
    {"color": [168, 171, 172], "isthing": 0, "id": 100, "name": "cardboard"},
    {"color": [146, 112, 198], "isthing": 0, "id": 107, "name": "counter"},
    {"color": [210, 170, 100], "isthing": 0, "id": 109, "name": "curtain"},
    {"color": [92, 136, 89], "isthing": 0, "id": 112, "name": "door-stuff"},
    {"color": [218, 88, 184], "isthing": 0, "id": 118, "name": "floor-wood"},
    {"color": [241, 129, 0], "isthing": 0, "id": 119, "name": "flower"},
    {"color": [217, 17, 255], "isthing": 0, "id": 122, "name": "fruit"},
    {"color": [124, 74, 181], "isthing": 0, "id": 125, "name": "gravel"},
    {"color": [70, 70, 70], "isthing": 0, "id": 128, "name": "house"},
    {"color": [255, 228, 255], "isthing": 0, "id": 130, "name": "light"},
    {"color": [154, 208, 0], "isthing": 0, "id": 133, "name": "mirror-stuff"},
    {"color": [193, 0, 92], "isthing": 0, "id": 138, "name": "net"},
    {"color": [76, 91, 113], "isthing": 0, "id": 141, "name": "pillow"},
    {"color": [255, 180, 195], "isthing": 0, "id": 144, "name": "platform"},
    {"color": [106, 154, 176], "isthing": 0, "id": 145, "name": "playingfield"},
    {"color": [230, 150, 140], "isthing": 0, "id": 147, "name": "railroad"},
    {"color": [60, 143, 255], "isthing": 0, "id": 148, "name": "river"},
    {"color": [128, 64, 128], "isthing": 0, "id": 149, "name": "road"},
    {"color": [92, 82, 55], "isthing": 0, "id": 151, "name": "roof"},
    {"color": [254, 212, 124], "isthing": 0, "id": 154, "name": "sand"},
    {"color": [73, 77, 174], "isthing": 0, "id": 155, "name": "sea"},
    {"color": [255, 160, 98], "isthing": 0, "id": 156, "name": "shelf"},
    {"color": [255, 255, 255], "isthing": 0, "id": 159, "name": "snow"},
    {"color": [104, 84, 109], "isthing": 0, "id": 161, "name": "stairs"},
    {"color": [169, 164, 131], "isthing": 0, "id": 166, "name": "tent"},
    {"color": [225, 199, 255], "isthing": 0, "id": 168, "name": "towel"},
    {"color": [137, 54, 74], "isthing": 0, "id": 171, "name": "wall-brick"},
    {"color": [135, 158, 223], "isthing": 0, "id": 175, "name": "wall-stone"},
    {"color": [7, 246, 231], "isthing": 0, "id": 176, "name": "wall-tile"},
    {"color": [107, 255, 200], "isthing": 0, "id": 177, "name": "wall-wood"},
    {"color": [58, 41, 149], "isthing": 0, "id": 178, "name": "water-other"},
    {"color": [183, 121, 142], "isthing": 0, "id": 180, "name": "window-blind"},
    {"color": [255, 73, 97], "isthing": 0, "id": 181, "name": "window-other"},
    {"color": [107, 142, 35], "isthing": 0, "id": 184, "name": "tree-merged"},
    {"color": [190, 153, 153], "isthing": 0, "id": 185, "name": "fence-merged"},
    {"color": [146, 139, 141], "isthing": 0, "id": 186, "name": "ceiling-merged"},
    {"color": [70, 130, 180], "isthing": 0, "id": 187, "name": "sky-other-merged"},
    {"color": [134, 199, 156], "isthing": 0, "id": 188, "name": "cabinet-merged"},
    {"color": [209, 226, 140], "isthing": 0, "id": 189, "name": "table-merged"},
    {"color": [96, 36, 108], "isthing": 0, "id": 190, "name": "floor-other-merged"},
    {"color": [96, 96, 96], "isthing": 0, "id": 191, "name": "pavement-merged"},
    {"color": [64, 170, 64], "isthing": 0, "id": 192, "name": "mountain-merged"},
    {"color": [152, 251, 152], "isthing": 0, "id": 193, "name": "grass-merged"},
    {"color": [208, 229, 228], "isthing": 0, "id": 194, "name": "dirt-merged"},
    {"color": [206, 186, 171], "isthing": 0, "id": 195, "name": "paper-merged"},
    {"color": [152, 161, 64], "isthing": 0, "id": 196, "name": "food-other-merged"},
    {"color": [116, 112, 0], "isthing": 0, "id": 197, "name": "building-other-merged"},
    {"color": [0, 114, 143], "isthing": 0, "id": 198, "name": "rock-merged"},
    {"color": [102, 102, 156], "isthing": 0, "id": 199, "name": "wall-other-merged"},
    {"color": [250, 141, 255], "isthing": 0, "id": 200, "name": "rug-merged"},
]

# fmt: off
COCO_PERSON_KEYPOINT_NAMES = (
    "nose",
    "left_eye", "right_eye",
    "left_ear", "right_ear",
    "left_shoulder", "right_shoulder",
    "left_elbow", "right_elbow",
    "left_wrist", "right_wrist",
    "left_hip", "right_hip",
    "left_knee", "right_knee",
    "left_ankle", "right_ankle",
)
# fmt: on

# Pairs of keypoints that should be exchanged under horizontal flipping
COCO_PERSON_KEYPOINT_FLIP_MAP = (
    ("left_eye", "right_eye"),
    ("left_ear", "right_ear"),
    ("left_shoulder", "right_shoulder"),
    ("left_elbow", "right_elbow"),
    ("left_wrist", "right_wrist"),
    ("left_hip", "right_hip"),
    ("left_knee", "right_knee"),
    ("left_ankle", "right_ankle"),
)

# rules for pairs of keypoints to draw a line between, and the line color to use.
KEYPOINT_CONNECTION_RULES = [
    # face
    ("left_ear", "left_eye", (102, 204, 255)),
    ("right_ear", "right_eye", (51, 153, 255)),
    ("left_eye", "nose", (102, 0, 204)),
    ("nose", "right_eye", (51, 102, 255)),
    # upper-body
    ("left_shoulder", "right_shoulder", (255, 128, 0)),
    ("left_shoulder", "left_elbow", (153, 255, 204)),
    ("right_shoulder", "right_elbow", (128, 229, 255)),
    ("left_elbow", "left_wrist", (153, 255, 153)),
    ("right_elbow", "right_wrist", (102, 255, 224)),
    # lower-body
    ("left_hip", "right_hip", (255, 102, 0)),
    ("left_hip", "left_knee", (255, 255, 77)),
    ("right_hip", "right_knee", (153, 255, 204)),
    ("left_knee", "left_ankle", (191, 255, 128)),
    ("right_knee", "right_ankle", (255, 195, 77)),
]

def _get_car_instances_meta():
    thing_ids = [k["id"] for k in CAR_CATEGORIES if k["isthing"] == 1]
    thing_colors = [k["color"] for k in CAR_CATEGORIES if k["isthing"] == 1]
    assert len(thing_ids) == 196, len(thing_ids)
    # Mapping from the incontiguous COCO category id to an id in [0, 79]
    thing_dataset_id_to_contiguous_id = {k: i for i, k in enumerate(thing_ids)}
    thing_classes = [k["name"] for k in CAR_CATEGORIES if k["isthing"] == 1]
    ret = {
        "thing_dataset_id_to_contiguous_id": thing_dataset_id_to_contiguous_id,
        "thing_classes": thing_classes,
        "thing_colors": thing_colors,
    }
    return ret

def _get_phone_instances_meta():
    thing_ids = [k["id"] for k in PHONE_CATEGORIES if k["isthing"] == 1]
    thing_colors = [k["color"] for k in PHONE_CATEGORIES if k["isthing"] == 1]
    assert len(thing_ids) == 3, len(thing_ids)
    # Mapping from the incontiguous COCO category id to an id in [0, 79]
    thing_dataset_id_to_contiguous_id = {k: i for i, k in enumerate(thing_ids)}
    thing_classes = [k["name"] for k in PHONE_CATEGORIES if k["isthing"] == 1]
    ret = {
        "thing_dataset_id_to_contiguous_id": thing_dataset_id_to_contiguous_id,
        "thing_classes": thing_classes,
        "thing_colors": thing_colors,
    }
    return ret

def _get_damage_instances_meta():
    thing_ids = [k["id"] for k in DAMAGE_CATEGORIES if k["isthing"] == 1]
    thing_colors = [k["color"] for k in DAMAGE_CATEGORIES if k["isthing"] == 1]
    assert len(thing_ids) == 4, len(thing_ids)
    # Mapping from the incontiguous COCO category id to an id in [0, 79]
    thing_dataset_id_to_contiguous_id = {k: i for i, k in enumerate(thing_ids)}
    thing_classes = [k["name"] for k in DAMAGE_CATEGORIES if k["isthing"] == 1]
    ret = {
        "thing_dataset_id_to_contiguous_id": thing_dataset_id_to_contiguous_id,
        "thing_classes": thing_classes,
        "thing_colors": thing_colors,
    }
    return ret

def _get_coco_instances_meta():
    thing_ids = [k["id"] for k in COCO_CATEGORIES if k["isthing"] == 1]
    thing_colors = [k["color"] for k in COCO_CATEGORIES if k["isthing"] == 1]
    assert len(thing_ids) == 80, len(thing_ids)
    # Mapping from the incontiguous COCO category id to an id in [0, 79]
    thing_dataset_id_to_contiguous_id = {k: i for i, k in enumerate(thing_ids)}
    thing_classes = [k["name"] for k in COCO_CATEGORIES if k["isthing"] == 1]
    ret = {
        "thing_dataset_id_to_contiguous_id": thing_dataset_id_to_contiguous_id,
        "thing_classes": thing_classes,
        "thing_colors": thing_colors,
    }
    return ret


def _get_coco_panoptic_separated_meta():
    """
    Returns metadata for "separated" version of the panoptic segmentation dataset.
    """
    stuff_ids = [k["id"] for k in COCO_CATEGORIES if k["isthing"] == 0]
    assert len(stuff_ids) == 53, len(stuff_ids)

    # For semantic segmentation, this mapping maps from contiguous stuff id
    # (in [0, 53], used in models) to ids in the dataset (used for processing results)
    # The id 0 is mapped to an extra category "thing".
    stuff_dataset_id_to_contiguous_id = {k: i + 1 for i, k in enumerate(stuff_ids)}
    # When converting COCO panoptic annotations to semantic annotations
    # We label the "thing" category to 0
    stuff_dataset_id_to_contiguous_id[0] = 0

    # 54 names for COCO stuff categories (including "things")
    stuff_classes = ["things"] + [
        k["name"].replace("-other", "").replace("-merged", "")
        for k in COCO_CATEGORIES
        if k["isthing"] == 0
    ]

    # NOTE: I randomly picked a color for things
    stuff_colors = [[82, 18, 128]] + [k["color"] for k in COCO_CATEGORIES if k["isthing"] == 0]
    ret = {
        "stuff_dataset_id_to_contiguous_id": stuff_dataset_id_to_contiguous_id,
        "stuff_classes": stuff_classes,
        "stuff_colors": stuff_colors,
    }
    ret.update(_get_coco_instances_meta())
    return ret


def _get_builtin_metadata(dataset_name):
    if dataset_name == "car":
        return _get_car_instances_meta()
    if dataset_name == "phone":
        return _get_phone_instances_meta()
    if dataset_name == "damage":
        return _get_damage_instances_meta()
    if dataset_name == "coco":
        return _get_coco_instances_meta()
    if dataset_name == "coco_panoptic_separated":
        return _get_coco_panoptic_separated_meta()
    elif dataset_name == "coco_person":
        return {
            "thing_classes": ["person"],
            "keypoint_names": COCO_PERSON_KEYPOINT_NAMES,
            "keypoint_flip_map": COCO_PERSON_KEYPOINT_FLIP_MAP,
            "keypoint_connection_rules": KEYPOINT_CONNECTION_RULES,
        }
    elif dataset_name == "cityscapes":
        # fmt: off
        CITYSCAPES_THING_CLASSES = [
            "person", "rider", "car", "truck",
            "bus", "train", "motorcycle", "bicycle",
        ]
        CITYSCAPES_STUFF_CLASSES = [
            "road", "sidewalk", "building", "wall", "fence", "pole", "traffic light",
            "traffic sign", "vegetation", "terrain", "sky", "person", "rider", "car",
            "truck", "bus", "train", "motorcycle", "bicycle", "license plate",
        ]
        # fmt: on
        return {
            "thing_classes": CITYSCAPES_THING_CLASSES,
            "stuff_classes": CITYSCAPES_STUFF_CLASSES,
        }
    raise KeyError("No built-in metadata for dataset {}".format(dataset_name))
