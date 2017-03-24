package gigasecond

import "time"

const testVersion = 4

const gigasecond = time.Duration(1000000000) * time.Second

func AddGigasecond(birthday time.Time) time.Time {
	return birthday.Add(gigasecond)

}
