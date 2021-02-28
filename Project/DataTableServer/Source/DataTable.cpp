
#include <iostream>

#include "data_table_def.hpp"

using namespace data;

int32 main()
{
	DataTableManager::GetInstance().Init();

    const ExampleDataTable* data_table_ptr = DATATABLE_GET_ROW(ExampleDataTable, 900000000);
    if (data_table_ptr) {
        std::cout << "DataId:" << data_table_ptr->DataId << std::endl;
        std::cout << "BoolType:" << data_table_ptr->BoolType << std::endl;
        std::cout << "Int32Type:" << data_table_ptr->Int32Type << std::endl;
        std::cout << "FloatType:" << data_table_ptr->FloatType << std::endl;
        std::cout << "StringType:" << data_table_ptr->StringType << std::endl;

        std::cout << "BitType:" << std::endl;
        std::cout << "(";
        int32 bit_value = data_table_ptr->BitType;
        bool is_first=true;
    	while(bit_value)
    	{
            if (is_first)
            {
                is_first = false;
            }
            else {
                std::cout << ",";
            }
            int32 bit_t = bit_value & 1;
            std::cout << bit_t;
            bit_value >>= 1;
    	}
        std::cout << ")" << std::endl;
    	
        std::cout << "VectorBoolType:" << std::endl;
        std::cout << "(";
        for (int32 i = 0; i < data_table_ptr->VectorBoolType.size(); i++) {
            if (i == 0) {
                std::cout << "";
            }
            else {
                std::cout << ",";
            }
            std::cout << data_table_ptr->VectorBoolType[i];
        }
        std::cout << ")" << std::endl;

        std::cout << "VectorInt32Type:" << std::endl;
        std::cout << "(";
        for (int32 i = 0; i < data_table_ptr->VectorInt32Type.size(); i++) {
            if (i > 0) {
                std::cout << ",";
            }
            std::cout << data_table_ptr->VectorInt32Type[i];
        }
        std::cout << ")" << std::endl;

        std::cout << "VectorFloatType:" << std::endl;
        std::cout << "(";
        for (int32 i = 0; i < data_table_ptr->VectorFloatType.size(); i++) {
            if (i > 0) {
                std::cout << ",";
            }
            std::cout << data_table_ptr->VectorFloatType[i];
        }
        std::cout << ")" << std::endl;

        std::cout << "VectorStringType:" << std::endl;
        for (int32 i = 0; i < data_table_ptr->VectorStringType.size(); i++) {
            std::cout << data_table_ptr->VectorStringType[i] << std::endl;
        }

    }

    system("pause");
    return 0;
}
