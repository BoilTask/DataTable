
#pragma once

namespace data
{
	template <typename T>
	class Singleton
	{
	protected:
		Singleton()
		{
		}
	protected:
		static T* instance_ptr_;

	public:
		static T& GetInstance()
		{
			if (!instance_ptr_)
			{
				instance_ptr_ = new T();
			}
			return *instance_ptr_;
		}
	};

	template <typename T>
	T* Singleton<T>::instance_ptr_ = nullptr;
}
