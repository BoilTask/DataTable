package dataparse

import (
	"strconv"
	"strings"
)

func ParseInt32(s string) int32 {
	v, _ := strconv.Atoi(s)
	return int32(v)
}

func ParseBool(s string) bool {
	v, _ := strconv.ParseBool(s)
	return v
}

func ParseFloat32(s string) float32 {
	n, _ := strconv.ParseFloat(s, 32)
	return float32(n)
}

func ParseString(s string) string {
	return s
}

func ParseVectorBool(s string) []bool {
	var v []bool
	if s == "" {
		return v
	}
	slice := strings.Split(s[1:len(s)-1], ",")
	for _, c := range slice {
		v = append(v, ParseBool(c))
	}
	return v
}

func ParseVectorInt32(s string) []int32 {
	var v []int32
	if s == "" {
		return v
	}
	slice := strings.Split(s[1:len(s)-1], ",")
	for _, c := range slice {
		v = append(v, ParseInt32(c))
	}
	return v
}

func ParseVectorFloat32(s string) []float32 {
	var v []float32
	if s == "" {
		return v
	}
	slice := strings.Split(s[1:len(s)-1], ",")
	for _, c := range slice {
		v = append(v, ParseFloat32(c))
	}
	return v
}

func ParseVectorString(s string) []string {
	var v []string
	if s == "" {
		return v
	}
	item := ""
	for i := 2; ; i++ {
		if i+1 >= len(s) {
			break
		}
		if s[i] == '\\' {
			if s[i+1] == '"' {
				item += "\""
				i++
			} else if s[i+1] == '\\' {
				item += "\\"
				i++
			}
		} else if s[i] == '"' {
			v = append(v, item)
			item = ""
			i += 2
		} else {
			item += string(s[i])
		}
	}
	return v
}
