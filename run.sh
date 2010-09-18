#!/usr/bin/env bash
java -jar tools/PlayGame.jar maps/map43.txt 1000 1000 log.txt "java -jar example_bots/RageBot.jar" "python MyBot.py" | java -jar tools/ShowGame.jar
