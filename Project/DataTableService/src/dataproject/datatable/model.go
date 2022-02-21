package datatable

type GameServerItem struct {
	Id     int32  `json:"id"`
	Serial string `json:"serial"`
	Name   string `json:"name"`
	Url    string `json:"url"`
	State  int32  `json:"state"`
}

type GameServerItemList []GameServerItem

func (list GameServerItemList) Swap(i, j int)      { list[i], list[j] = list[j], list[i] }
func (list GameServerItemList) Len() int           { return len(list) }
func (list GameServerItemList) Less(i, j int) bool { return list[i].Id < list[j].Id }
