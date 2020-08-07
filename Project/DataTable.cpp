
#include <iostream>

#include "game_macro.hpp"
#include "data_table_manager.h"

int main()
{
    DataTableManager::GetInstance().Init();

    const ConfigDataTable* data_table_ptr = DATATABLE_GET_DATA(ConfigDataTable, 101000000);
    if (data_table_ptr) {
        std::cout << "GameType:" << data_table_ptr->GameType << std::endl;
    }

    system("pause");
    return 0;
}
