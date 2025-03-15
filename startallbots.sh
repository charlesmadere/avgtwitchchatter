#!/bin/bash

declare -A bots
bots=(
    [avgjqchatter]=jaquarium
    [typbeevechatter]=beeve
    [whatachatter]=whataturtle
    [drewdybot]=drewdyboy
)

for bot in "${!bots[@]}"; do
    channel="${bots[$bot]}"
    xfce4-terminal --tab --title="$channel" --execute bash -c "./startbot.sh $bot $channel; exec bash"
done

