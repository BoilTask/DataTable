#ifndef __SINGLETON_HPP__
#define __SINGLETON_HPP__

namespace data {

	template<typename T>
	class Singleton {
	protected:
		Singleton() {}
	public:
		static T& GetInstance() {
			if (!m_pInstance) {
				m_pInstance = new T();
			}
			return *m_pInstance;
		}
	private:
		Singleton(Singleton& rhs) {};
		Singleton const& operator = (Singleton& rhs) {};
	protected:
		static T* m_pInstance;
	};

	template<typename T> T* Singleton<T>::m_pInstance = nullptr;
}

#endif //__SINGLETON_HPP__
