
cat ./AtomicCards.json | \
jq '[.data | .[] | .[] 
    | select(.legalities.commander == "Legal") 
    | select(.edhrecRank != null) 
    | select(.edhrecSaltiness != null) 
    |{
        name: .name,
        edhrecSaltiness: .edhrecSaltiness,
        edhrecRank: .edhrecRank,
    }]' > vis.json