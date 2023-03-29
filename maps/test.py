import engine

objects = engine.Map(
    walls=[
        engine.Wall((100, 100, 600, 100), "black_break_wall.png")
    ],
    surfaces=[
        engine.Surface((0, 0, 1200, 1000), "snow", "snow.png")
    ],
    roofs=[
        engine.Roof((0, 0, 1000, 1000), "default.png")
    ],
    map_start_point=[0, 0]
)
