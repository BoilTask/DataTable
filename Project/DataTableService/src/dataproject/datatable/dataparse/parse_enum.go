//Exported by Tool, please don't edit this file directly.

package dataparse

import (
	"dataproject/datatable/dataenum"
	"strings"
)

func ParseEnumEEnumType(s string) dataenum.EEnumType {
	return dataenum.EEnumType(ParseInt32(s))
}

func ParseVectorEnumEEnumType(s string) []dataenum.EEnumType {
	var v []dataenum.EEnumType
	if s == "" {
		return v
	}
	slice := strings.Split(s[1:len(s)-1], ", ")
	for _, c := range slice {
		v = append(v, dataenum.EEnumType(ParseInt32(c)))
	}
	return v
}

func ParseEnumEEnumType2(s string) dataenum.EEnumType2 {
	return dataenum.EEnumType2(ParseInt32(s))
}

func ParseVectorEnumEEnumType2(s string) []dataenum.EEnumType2 {
	var v []dataenum.EEnumType2
	if s == "" {
		return v
	}
	slice := strings.Split(s[1:len(s)-1], ", ")
	for _, c := range slice {
		v = append(v, dataenum.EEnumType2(ParseInt32(c)))
	}
	return v
}

func ParseEnumEEnumType3(s string) dataenum.EEnumType3 {
	return dataenum.EEnumType3(ParseInt32(s))
}

func ParseVectorEnumEEnumType3(s string) []dataenum.EEnumType3 {
	var v []dataenum.EEnumType3
	if s == "" {
		return v
	}
	slice := strings.Split(s[1:len(s)-1], ", ")
	for _, c := range slice {
		v = append(v, dataenum.EEnumType3(ParseInt32(c)))
	}
	return v
}

func ParseEnumETestType(s string) dataenum.ETestType {
	return dataenum.ETestType(ParseInt32(s))
}

func ParseVectorEnumETestType(s string) []dataenum.ETestType {
	var v []dataenum.ETestType
	if s == "" {
		return v
	}
	slice := strings.Split(s[1:len(s)-1], ", ")
	for _, c := range slice {
		v = append(v, dataenum.ETestType(ParseInt32(c)))
	}
	return v
}

func ParseEnumETestType2(s string) dataenum.ETestType2 {
	return dataenum.ETestType2(ParseInt32(s))
}

func ParseVectorEnumETestType2(s string) []dataenum.ETestType2 {
	var v []dataenum.ETestType2
	if s == "" {
		return v
	}
	slice := strings.Split(s[1:len(s)-1], ", ")
	for _, c := range slice {
		v = append(v, dataenum.ETestType2(ParseInt32(c)))
	}
	return v
}
